import streamlit as st
from resume_generator import generate_resume
from cover_letter_generator import generate_cover_letter

st.title("📄 AI Resume & Cover Letter Generator")

with st.form("user_input_form"):
    name = st.text_input("Your Name")
    job_role = st.text_input("Target Job Role")
    experience = st.text_area("Work Experience")
    skills = st.text_area("Skills")
    career_goals = st.text_area("Career Goals")
    company_name = st.text_input("Company (for cover letter)")
    
    submitted = st.form_submit_button("Generate")

if submitted:
    user_data = {
        "name": name,
        "job_role": job_role,
        "experience": experience,
        "skills": skills,
        "career_goals": career_goals,
        "company_name": company_name
    }

    st.subheader("📌 Generated Resume")
    st.write(generate_resume(user_data))

    st.subheader("📌 Generated Cover Letter")
    st.write(generate_cover_letter(user_data))
