# pages/about.py
import streamlit as st
st.set_page_config(
    page_title="About",  # Set page title
    page_icon="🌟",               # Set page icon
    layout="wide",                # Layout type (wide or centered)
    initial_sidebar_state="auto"  # Sidebar state (expanded, collapsed, or auto)
)
# About page content
st.markdown( """ <style> .css-1d391kg { background-color: #264cee; /* Desired background color */ } </style> """, unsafe_allow_html=True)
st.markdown( """ <style> .stApp { background: linear-gradient(0deg, rgb(250, 247, 240) 30%, rgba(176, 200, 255) 70%); } </style> """, unsafe_allow_html=True ) 
st.markdown( """ <style> /* Hide header */ header { visibility: hidden; } /* Hide footer */ .stFooter { visibility: hidden; } </style> """, unsafe_allow_html=True )
# About Page for Web Scraping App

st.title("About This Web Scraping App")

st.header("Overview")
st.write("""
This Web Scraping App is designed to **extract and analyze data from websites** efficiently. By automating the web scraping process and integrating with **Large Language Models (LLMs)**, the app simplifies data collection, summarization, and transformation.  
With just a URL, users can gather insights, extract valuable content, and even download results in structured formats.
""")

st.subheader("How It Works")
st.write("""
1. **Input a URL** – Paste the URL of the website you want to scrape.  
2. **Data Extraction** – The app scrapes text, articles, or structured content from the site.  
3. **LLM Processing** – Extracted data is processed by an LLM to summarize, analyze, or translate it.  
4. **Download & Use** – Results can be downloaded in CSV, or Texte format.
""")

st.subheader("Features")
st.write("""
- **Automated Scraping** – Extracts text from static and dynamic websites.  
- **AI Integration** – Leverages LLMs to summarize or process data.  
- **User-Friendly** – Simple interface with no coding required.  
- **Multiple Formats** – Export scraped data in different file formats.  
- **Scalable** – Handles multiple URLs and large websites seamlessly.  
""")

st.subheader("Why Choose This App?")
st.write("""
- **Efficiency** – Automates repetitive tasks and saves time.  
- **Accuracy** – Processes data using state-of-the-art language models.  
- **Ease of Use** – No programming skills required to scrape and analyze websites.  
- **Free to Use** – Fully functional and open-source for educational or professional use.  
""")

st.markdown("---")
st.write("🔗 **Start Scraping Now!** Navigate to the home page and begin extracting data effortlessly.")  

# Footer Section with Social Links
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        color: grey;
        text-align: center;
        padding: 10px;
        background-color: #D8D2C2;
    }
    .footer a {
        color: #4A90E2;
        text-decoration: none;
        margin: 0 10px;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        © 2025 Web_App_Scraping | 
        <a href="https://www.linkedin.com/in/ismail-najib/" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/Ismailnajib" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
