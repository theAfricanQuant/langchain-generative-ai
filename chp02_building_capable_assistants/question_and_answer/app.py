"""Question answering app in Streamlit.


Run locally as follows:
> PYTHONPATH=. streamlit run question_and_answer/app.py

Alternatively, you can deploy this on the Streamlit Community Cloud
or on Hugging Face Spaces. For Streamlit Community Cloud do this:
1. Create a GitHub repo
2. Go to Streamlit Community Cloud, click on "New app" and select the new repo
3. Click "Deploy!"
"""

import streamlit as st
import sys
# from pathlib import Path

# # Add the project root to PYTHONPATH
# sys.path.append(str(Path(__file__).parent.parent.parent.parent))

from langchain_community.callbacks.streamlit import (
    StreamlitCallbackHandler,
)

from agent import load_agent
from utils import MEMORY

st.set_page_config(page_title="LangChain Question Answering", page_icon=":robot:")
st.header("Ask a research question!")

strategy = st.radio(
    "Reasoning strategy",
    (
        "plan-and-solve",
        "zero-shot-react",
    ),
)

tool_names = st.multiselect(
    "Which tools do you want to use?",
    [
        "critical_search",
        "llm-math",
        "python_repl",
        "wikipedia",
        "arxiv",
        "google-search",
        "wolfram-alpha",
        "ddg-search",
    ],
    ["ddg-search", "wolfram-alpha", "wikipedia"],
)
if st.sidebar.button("Clear message history"):
    MEMORY.chat_memory.clear()

avatars = {"human": "user", "ai": "assistant"}
for msg in MEMORY.chat_memory.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

assert strategy is not None
agent_chain = load_agent(tool_names=tool_names, strategy=strategy)


if prompt := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_chain.invoke({"input": prompt}, {"callbacks": [st_callback]})
        st.write(response["output"])


import os

print(os.getcwd())
