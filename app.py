import streamlit as st
import pandas as pd
import re
from io import StringIO

def extract_details(resume_text):
    """Extract details from resume text."""
    details = {}

    # Extract name (assume it's the first line of the resume)
    name = resume_text.split("\n")[0].strip()
    details['Name'] = name

    # Extract email
    email = re.search(r'[\w.-]+@[\w.-]+\.\w+', resume_text)
    details['Email'] = email.group(0) if email else 'Not found'

    # Extract phone number
    phone = re.search(r'\+?\d[\d\s()-]{7,}', resume_text)
    details['Phone'] = phone.group(0) if phone else 'Not found'

    # Extract field of study and internship application
    if "Bachelor of Arts" in resume_text:
        details['Field'] = "Student of Science and Maths applying for an internship in coding"
    else:
        details['Field'] = 'Not found'

    # Extract skills (example keywords, customize as needed)
    skills_keywords = ["Python", "Java", "C++", "Machine Learning", "Data Analysis", "SQL", "Communication"]
    skills_found = [skill for skill in skills_keywords if skill.lower() in resume_text.lower()]
    details['Skills'] = skills_found if skills_found else 'Not found'

    return details

def check_projects_in_resume(resume_text, projects):
    """Check if projects from the Excel file are mentioned in the resume."""
    missing_projects = []
    for project in projects:
        if project.lower() not in resume_text.lower():
            missing_projects.append(project)
    return missing_projects

def main():
    st.title("Resume Parsing and Validation Application")
    st.write("Upload a text file of a resume and an Excel file containing project details. The application will extract details and validate projects.")

    # Upload Excel file
    excel_file = st.file_uploader("Upload Excel file with project details", type=["xlsx"])
    if excel_file is not None:
        try:
            df = pd.read_excel(excel_file)
            st.write("Excel file loaded successfully!")
            st.dataframe(df)
            
            # Ensure 'Projects' column exists
            if 'Projects' not in df.columns:
                st.error("The Excel file must contain a 'Projects' column.")
                return

            projects = df['Projects'].dropna().tolist()
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")
            return
    else:
        st.warning("Please upload an Excel file.")
        return

    # Upload text file
    uploaded_file = st.file_uploader("Choose a text file (Resume)", type=["txt"])

    if uploaded_file is not None:
        # Read the text file
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        resume_text = stringio.read()

        # Parse the resume
        with st.spinner("Extracting details..."):
            details = extract_details(resume_text)

        # Display extracted details
        st.subheader("Extracted Details")
        for key, value in details.items():
            st.write(f"**{key}:** {value}")

        # Validate projects
        with st.spinner("Validating projects..."):
            missing_projects = check_projects_in_resume(resume_text, projects)

        st.subheader("Project Validation")
        if missing_projects:
            st.write("The following projects from the Excel file are missing in the resume:")
            for project in missing_projects:
                st.write(f"- {project}")
        else:
            st.write("All projects from the Excel file are mentioned in the resume.")

if __name__ == "__main__":
    main()
