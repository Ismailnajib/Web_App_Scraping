import streamlit as st
import pandas as pd
import nest_asyncio
import asyncio
import os
from groq import Groq
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup


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
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text and try to organize the data as table as possible."
)

# Function to scrape the website using Playwright (asynchronous)
async def scrape_website(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Launch browser
        page = await browser.new_page()
        await page.goto(url)
        html_content = await page.content()  # Get the page content
        await browser.close()  # Close the browser
        return html_content


# Function to extract body content from HTML
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


# Function to clean the body content
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator='\n') 
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.split())
    return cleaned_content


# Function to split DOM content into manageable chunks
def split_dom_content(dom_content, max_length=7000):
    return [dom_content[i: i+max_length] for i in range(0, len(dom_content), max_length)]


# Function to parse text using the Groq Llama3 model
def parse_with_groq(dom_chunks, parse_description):
    parsed_results = []
    for i, chunk in enumerate(dom_chunks, start=1):
        # Format the prompt with the provided chunk and description
        prompt_text = template.format(dom_content=chunk, parse_description=parse_description)

        # Send the request to Groq's model
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt_text}],
            model="llama3-70b-8192"  # The Llama model used for parsing
        )

        # Assuming 'content' is directly accessible without using .get()
        if response.choices and hasattr(response.choices[0].message, 'content'):
            result = response.choices[0].message.content
        else:
            result = ''

        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(result)

    # Join all parsed results into a single string and return it
    return "\n".join(parsed_results)


# Function to convert parsed results into CSV format
def convert_table_to_csv(parsed_results, encoding='utf-8'):
    lines = parsed_results.strip().split('\n')
    columns = [col.strip() for col in lines[0].split(' ')[1:-1]]  # Extract column names

    # Initialize an empty list for rows
    data = []
    for line in lines[2:]:
        row = [value.strip() if value.strip() != '' else None for value in line.split('|')[1:-1]]
        
        if len(row) != len(columns):
            # Adjust row length if necessary
            if len(row) < len(columns):
                row += [None] * (len(columns) - len(row))
            else:
                row = row[:len(columns)]  # Trim extra columns if there are too many
        
        data.append(row)

    # Create DataFrame from data and columns, then return CSV
    df = pd.DataFrame(data, columns=columns)
    return df.to_csv(index=False, encoding=encoding)


# Main function for Streamlit app
async def main():
    st.set_page_config(
        page_title="Home",  # Set page title
        page_icon="🌟",  # Set page icon
        layout="wide",  # Layout type (wide or centered)
        initial_sidebar_state="auto"  # Sidebar state
    )

    # Custom CSS to style the page
    st.markdown("""<style> .css-1d391kg { background-color: #264cee; } </style>""", unsafe_allow_html=True)
    st.markdown("""<style> .stApp { background: linear-gradient(0deg, rgb(250, 247, 240) 30%, rgba(176, 200, 255) 70%); } </style>""", unsafe_allow_html=True)
    st.markdown("""<style> header { visibility: hidden; } .stFooter { visibility: hidden; } </style>""", unsafe_allow_html=True)

    # Page title and description
    st.title("Web App Scraping with LLM")
    st.subheader("By bridging web scraping and LLM capabilities, this app serves as a powerful tool for data-driven applications.")

    # Input for website URL
    url = st.text_input("Enter a website URL:")

    # Scraping logic when the button is pressed
    if st.button("Scrape"):
        st.write("Loading data...")
        if url:
            html_content = await scrape_website(url)
            
            # Process the content
            body_content = extract_body_content(html_content)
            cleaned_content = clean_body_content(body_content)
            
            # Store cleaned content in session state
            st.session_state.dom_content = cleaned_content
        else:
            st.write("The URL is empty!")

    # If content is scraped, allow parsing and display results
    if "dom_content" in st.session_state:
        parse_description = st.text_area("Describe what you want to parse:")
        
        if st.button("Parse Content"):
            if parse_description:
                st.write("Parsing the content...")
                
                # Split content into chunks and parse based on description
                dom_chunks = split_dom_content(st.session_state.dom_content)
                parsed_result = parse_with_groq(dom_chunks, parse_description)
                
                # Display parsed result
                st.write(parsed_result)

                # Download parsed result as .txt
                st.download_button(
                    label="Download txt",
                    data=parsed_result,
                    file_name="data_texte.txt",
                    mime="text/plain"
                )

                # Convert parsed results to CSV and download
                csv_data = convert_table_to_csv(parsed_result)
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="data_csv.csv",
                    mime="csv"
                )
            else:
                st.write("Please provide a description to parse.")


# Apply nest_asyncio to allow running within the existing event loop
nest_asyncio.apply()
asyncio.run(main())











    











