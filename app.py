import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎓 Free Admissions Assistant")

question = st.text_input("Ask an admissions question")

if question:
    prompt = f"""
You are a helpful university admissions assistant for high school students.

Question: {question}

Give a concise answer and encourage checking the official university website.
"""

    response = model.generate_content(prompt)

    st.write(response.text)

    st.caption("General guidance only — verify with official admissions websites.")
