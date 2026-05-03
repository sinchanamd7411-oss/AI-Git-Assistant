# AI Git Assistant

This is an AI-powered Git assistant that helps with generating commit messages and other Git-related tasks using OpenAI's GPT models.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the assistant:
```
python main.py
```

The assistant will analyze your current Git changes and suggest a commit message.