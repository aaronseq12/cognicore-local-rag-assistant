import streamlit as st
import requests

st.set_page_config(page_title="CogniCore Local", page_icon="🧠", layout="wide")
st.title("`CogniCore` - 100% Local Assistant ")
st.markdown("This assistant is running completely on your local machine. Your data never leaves your computer.")

query = st.text_input(
    "**Ask a question about your documents:**", 
    placeholder="e.g., What is Project Phoenix?"
)

if query:
    with st.spinner("Searching and thinking..."):
        try:
            response = requests.post("http://127.0.0.1:8000/query", json={"text": query})
            if response.status_code == 200:
                st.success("**Answer:**")
                st.write(response.json()['answer'])
            else:
                st.error(f"API Error: {response.status_code}")
        except requests.exceptions.RequestException:
            st.error("Could not connect to the backend API. Is it running?")