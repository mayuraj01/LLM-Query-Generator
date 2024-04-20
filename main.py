from langchain.llms.openai import OpenAI
import streamlit as st
from langchain_helper import get_shot_db_chain

st.title("Cloth Store Database Q&A")

question=st.text_input("Question: ")

if question:
    chain=get_shot_db_chain()
    answer=chain.run(question)
    st.header("Answer: ")
    st.write(answer)

