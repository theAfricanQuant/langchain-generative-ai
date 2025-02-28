# langchain-generative-ai
Working thru Generative AI with LangChain

I am following thru the book, [Generatiive AI with Langchain](https://github.com/benman1/generative_ai_with_langchain) by Ben Auffarth. I am using the book to understand further how to use OpenAI's GPT-3 and Huggingface's Transformers to create chatbots and everything else they offer.

This is not a comprehensive guide to the book, but a way to document my journey thru the book and the things I learn along the way. You may need to purchase your own copy to get the full experience. I may start something and get tired or bored or uninterested and you might be left wondering what happened. I am not obligated to finish the book or the project. I am doing this for fun and to learn something new. Especially since I have a similar project looking me in the eye to complete

## Setting up the environment

Here is how I would setup my environment to work thru the book. Mine has a lil twist to it because I am using a different environment manager, to manage my environment.

I would make sure I set up my environment with [uv from astral](https://astral.sh/blog/uv-unified-python-packaging). You could also use pip, conda, poetry, or docker!

I would also creat a `.env` file to store my API keys and make sure to include a `.gitignore` file that would exclude my `.env` from being added to my Git repository.
```python
# .env
OPENAI_API_KEY="your-openai-api-key"
HUGGINGFACEHUB_API_TOKEN="your-huggingfacehub-api-token"
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