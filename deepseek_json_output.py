import json
import os
from typing import Dict, List, Any
from dataclasses import dataclass
from dotenv import load_dotenv
from openai import OpenAI

@dataclass
class DeepseekConfig:
    """Configuration settings for Deepseek API"""
    api_key: str
    base_url: str = "https://api.deepseek.com"
    model_name: str = "deepseek-chat"

class QuestionAnswerParser:
    """Handles parsing of questions and answers using Deepseek API"""

    SYSTEM_PROMPT = """
    The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

    EXAMPLE INPUT: 
    Which is the highest mountain in the world? Mount Everest.

    EXAMPLE JSON OUTPUT:
    {
        "question": "Which is the highest mountain in the world?",
        "answer": "Mount Everest"
    }
    """

    def __init__(self, config: DeepseekConfig):
        """Initialize parser with configuration"""
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )
        self.model_name = config.model_name

    def _create_messages(self, user_input: str) -> List[Dict[str, str]]:
        """Create message structure for API request"""
        return [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]

    def parse_qa(self, text: str) -> Dict[str, str]:
        """
        Parse question and answer from input text

        Args:
            text: Input text containing question and answer

        Returns:
            Dictionary containing parsed question and answer

        Raises:
            ValueError: If API request fails or response is invalid
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self._create_messages(text),
                response_format={'type': 'json_object'}
            )

            return json.loads(response.choices[0].message.content)

        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON response: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error processing request: {str(e)}")

def initialize_config() -> DeepseekConfig:
    """Initialize and validate configuration from environment variables"""
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable must be set")
    return DeepseekConfig(api_key=api_key)

def main() -> None:
    try:
        # Initialize configuration
        config = initialize_config()

        # Create parser instance
        parser = QuestionAnswerParser(config)

        # Example input text
        input_text = "Which is the longest river in the world? The Nile River."

        # Parse question and answer
        result = parser.parse_qa(input_text)

        # Pretty print the result
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
