import streamlit as st
from google import genai

# Connect to Gemini
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Page
st.set_page_config(
    page_title="Admissions Assistant",
    page_icon="🎓"
)

st.title("🎓 Free Admissions Assistant")

st.write(
    "Ask questions about university admissions, programs, "
    "requirements, applications, and more."
)

question = st.text_input(
    "Ask an admissions question"
)

if question:
    prompt = f"""
You are a helpful university admissions assistant for high school students.

The student asked:
{question}

Give a clear, concise answer that is easy for a high school student
to understand.

Do not invent university requirements, deadlines, statistics, or policies.
If you are uncertain, explicitly say that you are uncertain.

Encourage the student to verify important information on the
university's official admissions website.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    st.write(response.text)

    st.caption(
        "General guidance only — always verify important information "
        "with the official university website."
    )
