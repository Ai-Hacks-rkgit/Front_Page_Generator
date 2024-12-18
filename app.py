import streamlit as st
from pdf_generator import Generate_pdf
import time
import os


st.set_page_config(
    page_title="Front Page Generator",
    page_icon=":material/smart_toy:" 
)

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

    progress_text = "Generating PDF. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    with open(outputfile, "rb") as file:
        btn = st.download_button(
            label="Download PDF",
            data=file,
            file_name=outputfile,
            mime="application/octet-stream"
        )

    time.sleep(120)
    os.remove(outputfile)
