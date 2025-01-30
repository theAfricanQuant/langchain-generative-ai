# langchain-generative-ai
Working thru Generative AI with LangChain

I am following thru the book, [Generatiive Ai with Langchain by Ben Auffarth](https://github.com/benman1/generative_ai_with_langchain). I am using the book to learn how to use OpenAI's GPT-3 and Huggingface's Transformers to create a chatbot. I am also using the book to learn how to use the OpenAI API and the Huggingface Hub API.

Here is how I would setup my environment to work thru the book. Mine has a lil more twist to it because I am using a different environment manager, to manage my environment.

I would make sure I set up my environment with [uv from astral](https://astral.sh/blog/uv-unified-python-packaging). You could also use pip, conda, poetry, or docker!

I would also creat a `.env` file to store my API keys and make sure to include a `.gitignore` file that would exclude my `.env` from being added to my Git repository.
```python
# .env
OPENAI_API_KEY="your-openai-api-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingface-api-token"
```

You can set up the keys for the different providers with a config.py like this:
```python
# config.py
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Extract the variables from the .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Function to set environment variables (optional, if you want to ensure they are set in the system environment)
def set_environment():
    variable_dict = globals().items()
    for key, value in variable_dict:
        if "API" in key or "TOKEN" in key:
            os.environ[key] = value

```

You can next can next call the set_environment() function to set the environment variables in the system environment.

```python
# app.py or main.py or any other file
from config import set_environment
set_environment()
```