import streamlit as st
from langchain.prompts import PrompTemplate
from langchain.llms import CTransformers

#Function to get response from llama model
def getllama(input_text,law,crime_type):
    





st.set_page_config(
    page_title="Legal Advisor",
    page_icon=":D",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.header("Generate the answers")

input_text = st.text_input("Enter your question")
col1, col2 = st.columns([5,5])

with col1:
    law = st.text_input("Which law is affected")
with col2:
    crime_type = st.selectbox("Whats the crime type",("Civil law","Criminal law","Fundamental rights"), index = 0)

submit = st.button("Generate")


if submit:
    st.write(getllama(input_text,law,crime_type))