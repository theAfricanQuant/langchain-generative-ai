# setting the environment variables
import sys
import os

sys.path.insert(0, os.path.abspath(".."))

from config import set_environment

set_environment()

from langchain_openai import OpenAI

llm = OpenAI()

summary = llm.invoke("Tell me a joke about light bulbs!")

print(summary)

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize the chat model:
llm = ChatOpenAI(model_name="gpt-4-0613")
# Generate a conversation:
response = llm.invoke([HumanMessage(content='Say "Hello world" in Python.')])
print(response)

from langchain_core.messages import SystemMessage

chat_output = llm.invoke(
    [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(content="What is the purpose of model regularization?"),
    ]
)
print(chat_output)

prompt = """
Summarize this text in one sentence:
{text}
"""
llm = OpenAI()
summary = llm.invoke(prompt.format(text="Some long story"))
print(summary)

from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.5,
)
template = """Question: {question} Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)
runnable = prompt | llm | StrOutputParser()

question = "Who won the FIFA World Cup in the year 1994? "
summary = runnable.invoke({"question": question})

print(summary)
