import streamlit as st
from pdf_generator import Generate_pdf
import time
import os

# Hide the default Streamlit menu
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    #GithubIcon {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.write("""
# Lab File Front Page Generator
Create a front page for your lab assignment.
""")

name=st.text_input("Name")
roll_no = st.text_input("Roll No")
department = st.text_input("Branch ex: CSE AIML")
year = st.text_input("Year of Study ex: 3rd Year")
session=st.text_input("Session ex:2025-26")
teacher=st.text_input("Teacher Name")
subject=st.text_input("Lab Name and Lab code")

if st.button("Generate PDF"):
    Generate_pdf(name,roll_no,department,session,teacher,subject,year)

    outputfile=name+"_"+subject+"_"+"file"+".pdf"

    with open(outputfile, "rb") as file:
        btn = st.download_button(
            label="Download PDF",
            data=file,
            file_name=outputfile,
            mime="application/octet-stream"
        )

    time.sleep(120)
    os.remove(outputfile)
