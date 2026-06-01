import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📧 AI Email Generator")
st.write("Generate professional emails using Gemini AI")

purpose = st.text_input("Email Purpose")

details = st.text_area("Enter Details")

company_name = st.text_input("Company Name")

tone = st.selectbox(
    "Select Email Tone",
    ["Professional", "Formal", "Friendly"]
)

email_type = st.selectbox(
    "Select Email Type",
    [
        "Job Application",
        "Leave Request",
        "Internship Request",
        "Meeting Request",
        "Project Update"
    ]
)

email_length = st.selectbox(
    "Email Length",
    ["Short", "Medium", "Detailed"]
)

generate = st.button("🚀 Generate Email")

if generate:

    prompt = f"""
    Generate a professional email.
    
    Company Name: {company_name}

    Email Type: {email_type}

    Tone: {tone}
    
    Email Length: {email_length}

    Purpose: {purpose}

    Details: {details}

    Include:
    1. Subject
    2. Greeting
    3. Professional Email Body
    4. Closing
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Email")

    st.text_area(
    "Generated Email",
    response.text,
    height=300
)
    st.download_button(
    label="📥 Download Email",
    data=response.text,
    file_name="generated_email.txt",
    mime="text/plain"
)

