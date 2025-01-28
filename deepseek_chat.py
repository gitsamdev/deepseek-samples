import os
from dotenv import load_dotenv
from openai import OpenAI

# Initialize the OpenAI client with Deepseek's API base
load_dotenv()
if not os.getenv("DEEPSEEK_API_KEY"):
    raise ValueError("DEEPSEEK_API_KEY environment variable must be set")

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(prompt):
    """
    Send a chat request to Deepseek API using OpenAI SDK
    
    Args:
        prompt (str): The input prompt to send to the model
        
    Returns:
        str: The model's response or an error message
    """
    if not prompt or not isinstance(prompt, str):
        return "Error: Invalid prompt provided"
        
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # Use appropriate model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7  # Add temperature for better response quality
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Check if API key is set
    if not os.getenv("DEEPSEEK_API_KEY"):
        print("Error: DEEPSEEK_API_KEY environment variable is not set")
        return

    # Example usage
    prompt = "What is artificial intelligence?"
    response = chat_with_deepseek(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()