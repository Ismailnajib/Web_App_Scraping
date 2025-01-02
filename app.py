# app.py
import streamlit as st
import pandas as pd
import os
import re
import csv
import requests
from groq import Groq
from selenium.webdriver import ChromeOptions, Remote
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

def scrape_website(website):
 
        chrome_driver_path = r"./chromedriver.exe"
        options = ChromeOptions()
        options.add_argument("--no-sandbox")  # Bypass OS-level sandbox
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources issues
        options.add_argument("--disable-gpu")  # Disable GPU acceleration
        options.add_argument("--remote-debugging-port=9222")  # Debugging port # Set a window size to avoid element not found issues
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options) 
        try:
            driver.get(website)
            print("page loaded ...")
            html= driver.page_source
            return html
        finally:
            driver.quit()
#############################################################################

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
         return str(body_content)
    return ""

################################################################################

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(['script', 'style']):
         script_or_style.extract()
    
    cleaned_content = soup.get_text(separator='\n') 
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.split()
    )
    return cleaned_content


###############################################################################

def split_dom_content(dom_content, max_lenght=7000):
    return [
     dom_content[i: i+max_lenght] for i in range(0, len(dom_content), max_lenght)
    ]    


####################################################################################


import os
from groq import Groq

# Set the API key in the environment (for production, set it securely in your environment)
os.environ["API_KEYQ"] = "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"

# Initialize the Groq client with API key
client = Groq(api_key=os.getenv("API_KEYQ"))

# Template for extracting information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text and try to orgnize the data as table as possible."
)

# Function to parse text using the Groq Llama3 model
def parse_with_groq(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        # Format the prompt with the provided chunk and description
        prompt_text = template.format(dom_content=chunk, parse_description=parse_description)

        # Send the request to Groq's model
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="llama3-70b-8192"          #llama-3.2-90b-vision-preview
        )

        # Assuming 'content' is directly accessible without using `.get()`
        if response.choices and hasattr(response.choices[0].message, 'content'):
            result = response.choices[0].message.content
        else:
            result = ''

        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(result)

    # Join all parsed results into a single string and return it
    return "\n".join(parsed_results)


# Function to convert the table format to CSV with encoding
def convert_table_to_csv(parsed_results, encoding='utf-8'):
    # Split the table into lines and clean up the column headers
    lines = parsed_results.strip().split('\n')
    
    # Extract columns, removing the first and last '|' symbol, and trimming spaces
    columns = [col.strip() for col in lines[0].split(' ')[1:-1]]
    
    # Initialize an empty list to store rows
    data = []
    
    # Iterate over the table lines (skipping the header and separator lines)
    for line in lines[2:]:
        # Split row values by the pipe character and clean up the spaces
        row = [value.strip() if value.strip() != '' else None for value in line.split('|')[1:-1]]
        
        # Ensure the row has the same number of columns as the header
        if len(row) != len(columns):
            # Adjust row length if necessary
            if len(row) < len(columns):
                row += [None] * (len(columns) - len(row))  # Fill missing columns with None
            else:
                row = row[:len(columns)]  # Trim extra columns if there are too many
        
        data.append(row)
    
    # Create a DataFrame from the data list and columns
    df = pd.DataFrame(data, columns=columns)
    
    # Convert the DataFrame to CSV format with the specified encoding (UTF-8 by default)
    csv_data = df.to_csv(index=False, encoding=encoding)
    
    return csv_data

#############################################################


# Set page configuration (must be the first Streamlit command)

st.set_page_config(
    page_title="Home",  # Set page title
    page_icon="🌟",               # Set page icon
    layout="wide",                # Layout type (wide or centered)
    initial_sidebar_state="auto"  # Sidebar state (expanded, collapsed, or auto)
)
st.markdown( """ <style> .css-1d391kg { background-color: #264cee; /* Desired background color */ } </style> """, unsafe_allow_html=True)
st.markdown( """ <style> .stApp { background: linear-gradient(0deg, rgb(250, 247, 240) 30%, rgba(176, 200, 255) 70%); } </style> """, unsafe_allow_html=True ) 
st.markdown( """ <style> /* Hide header */ header { visibility: hidden; } /* Hide footer */ .stFooter { visibility: hidden; } </style> """, unsafe_allow_html=True )
st.title("Web App Scraping with LLM")
st.subheader("By bridging web scraping and LLM capabilities, this app serves as a powerful tool for data-driven applications in today’s information-rich environment.")

url = st.text_input("Enter a website URL :")

if st.button("Scrape"):
    st.write("loading data")
    if url:
        result= scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        st.session_state.dom_content = cleaned_content
    else :
        st.write("the url is empty !!!")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descrive What you want to parse ? " )
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content ...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_groq(dom_chunks, parse_description)
            #st.text_area("DOM CONTENT",parsed_result, height=300  )
            st.write(parsed_result)

        st.download_button(
        label="Download txt",
        data=parsed_result,
        file_name="data_texte.txt",
        mime="text/plain"
        )
        csv_data = convert_table_to_csv(parsed_result)

        # Add a download button for the CSV data
        # Custom CSS for Download Button
        
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="data_csv.csv",
            mime="csv"
        )

        











