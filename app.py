import streamlit as st
from google import genai

# Gemini client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Load Waterloo knowledge base
with open("universities/waterloo.txt", "r") as f:
    waterloo_info = f.read()

st.set_page_config(
    page_title="Ontario Admissions Assistant",
    page_icon="🎓"
)

st.title("🎓 Ontario Admissions Assistant")

st.write(
    "Ask questions about Ontario university admissions."
)

question = st.text_input(
    "Ask an admissions question"
)

if question:

    prompt = f"""
You are an Ontario university admissions assistant.

Use the official Waterloo admissions information below when answering
questions related to the University of Waterloo.

OFFICIAL WATERLOO INFORMATION:
{waterloo_info}

Student question:
{question}

Instructions:
- Answer in plain English for a high school student.
- If the question is about Waterloo, use the official information above.
- Do not invent admission averages or guarantees.
- Mention that requirements can change yearly.
- Include the official Waterloo source link when relevant.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    st.markdown("### Answer")
    st.write(response.text)

    st.caption(
        "General guidance only — verify important information on the official university website."
    )
