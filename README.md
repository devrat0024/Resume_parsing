Resume Parsing and Validation App
This project is a Streamlit-based web application that parses a candidate’s resume to extract key details and validate listed projects against an Excel file. It helps recruiters and hiring teams verify if the applicant has included all expected projects in their resume.

🔍 Features
Upload a .txt resume and an .xlsx file with project names.

Extract important details like:

Name

Email

Phone Number

Field of Study

Skills

Validate if the projects listed in the Excel file are mentioned in the resume.

User-friendly web interface built with Streamlit.

🛠️ Technologies Used
Python 3

Streamlit

pandas

re (Regular Expressions)

openpyxl (for reading Excel files)

📁 Project Structure
bash
Copy
Edit
├── app.py               # Main Streamlit application
├── app.xlsx             # Sample Excel file with project list
├── app.txt              # Sample resume in text format
⚙️ How to Run
Clone the repository or download the files.

Install required packages:

bash
Copy
Edit
pip install streamlit pandas openpyxl
Run the app:

bash
Copy
Edit
streamlit run app.py
📄 Usage
Upload your Excel file containing the list of expected project names (with a column named Projects).

Upload a .txt version of a resume.

The app will display extracted candidate details and highlight any missing projects.

📌 Notes
Ensure the resume is saved in plain text format (.txt).

The Excel file must include a column named "Projects".
