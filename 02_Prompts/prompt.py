from dotenv import load_dotenv
import os
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# ----------------------------
# Streamlit Config
# ----------------------------
st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Paper Assistant")
st.markdown(
    "Analyze any AI/ML research paper using **Google Gemini + LangChain**."
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("⚙ Settings")

style = st.sidebar.selectbox(
    "Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

difficulty = st.sidebar.selectbox(
    "Difficulty Level",
    [
        "School Student",
        "College Student",
        "AI Beginner",
        "AI Engineer",
        "Researcher"
    ]
)

length = st.sidebar.selectbox(
    "Response Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)

include_code = st.sidebar.checkbox("Include Code Example")

include_math = st.sidebar.checkbox("Include Mathematical Explanation")

include_questions = st.sidebar.checkbox("Generate Interview Questions")

include_similar = st.sidebar.checkbox("Recommend Similar Papers")

include_quiz = st.sidebar.checkbox("Generate Quiz")

# ----------------------------
# User Input
# ----------------------------
paper = st.text_input(
    "📄 Enter Research Paper Name",
    placeholder="Example: Attention Is All You Need"
)

# ----------------------------
# Prompt
# ----------------------------
template = PromptTemplate(
    input_variables=[
        "paper",
        "style",
        "difficulty",
        "length",
        "code",
        "math",
        "questions",
        "similar",
        "quiz"
    ],
    template="""
You are an expert AI Research Scientist.

Generate a professional report on the following research paper.

Research Paper:
{paper}

Explanation Style:
{style}

Difficulty Level:
{difficulty}

Length:
{length}

Include Code Example:
{code}

Include Mathematical Explanation:
{math}

Generate Interview Questions:
{questions}

Recommend Similar Papers:
{similar}

Generate Quiz:
{quiz}

Your report MUST contain:

# 📄 Abstract

# 🎯 Problem Statement

# 💡 Motivation

# 🏗 Model Architecture

# ⚙ Working Process

# 🧠 Key Contributions

# 📊 Dataset Used

# 📈 Results

# 👍 Advantages

# 👎 Limitations

# 🌍 Real-world Applications

# 🚀 Future Scope

# 📚 Similar Papers

# 💻 Code Example

# 📐 Mathematical Explanation

# 🎤 Interview Questions

# 📝 Quiz

# 📖 Conclusion

Use markdown headings.

Use bullet points.

Explain clearly.
"""
)

# ----------------------------
# Generate Report
# ----------------------------
if st.button("🚀 Analyze Paper"):

    if paper == "":
        st.warning("Please enter a research paper name.")
        st.stop()

    chain = template | model

    with st.spinner("Analyzing Research Paper..."):

        result = chain.invoke(
            {
                "paper": paper,
                "style": style,
                "difficulty": difficulty,
                "length": length,
                "code": include_code,
                "math": include_math,
                "questions": include_questions,
                "similar": include_similar,
                "quiz": include_quiz,
            }
        )

    st.success("Analysis Complete!")

    st.markdown(result.content)

    st.download_button(
        "📥 Download Report",
        result.content,
        file_name="Research_Report.md",
        mime="text/markdown"
    )