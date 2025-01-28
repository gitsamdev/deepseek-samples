# DeepSeek Chat API Sample

This repository demonstrates how to use the DeepSeek Chat API with Python. It includes sample code for interacting with DeepSeek's language models through their API.

## Prerequisites

- Python 3.8 or higher
- A DeepSeek API key (sign up at https://platform.deepseek.com)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/gitsamdev/deepseek-samples.git
   cd deepseek-samples
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install python-dotenv openai
   ```

4. Create a `.env` file in the project root and add your DeepSeek API key:
   ```
   DEEPSEEK_API_KEY=your_api_key_here
   ```

## Running the Sample

The repository includes a sample script that demonstrates how to use the DeepSeek Chat API:

```bash
python deepseek_chat.py
```

This will run a simple example that asks the model "What is artificial intelligence?" and prints the response.

## Code Structure

- `deepseek_chat.py`: Contains the main implementation for interacting with the DeepSeek Chat API
  - Uses OpenAI's SDK with DeepSeek's API endpoint
  - Includes error handling and environment variable validation
  - Demonstrates how to make chat completions requests

## Environment Variables

- `DEEPSEEK_API_KEY`: Your DeepSeek API key (required)

## Error Handling

The code includes basic error handling for:
- Missing API key
- Invalid prompts
- API request failures

## Additional Resources

- [DeepSeek Platform Documentation](https://platform.deepseek.com/docs)
- [OpenAI SDK Documentation](https://github.com/openai/openai-python)
