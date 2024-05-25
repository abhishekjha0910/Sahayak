
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]=os.getenv("langchain")

#Promp template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . please responce to the user queries"),
        ("user","Question:{question}")
    ]
)

#streamlet framework
st.title('langchain Demo With ollama')
input_text = st.text_input("Search the topic u want")


#ollama llm
llm = Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))