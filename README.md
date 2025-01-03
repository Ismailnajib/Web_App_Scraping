# Web_App_Scraping
This is a free solution for web app scraping, allowing you to extract text from any platform.


Objective: To develop a user-friendly web app that allows users to input a URL, scrape and process the content, and extract relevant data. 

# Creation of project step by step

## Phase 1: Setup and Environment
### 1: Define Requirements:
* Define the scraping needs: URL input, text extraction, NER.
* Specify the output formats (CSV, TXT) and tools (Selenium,streamlit, groq, beautifulsoup4, pyppeteer, spaCy, pandas ...).
* The project begins with setting up a dedicated virtual environment and installing necessary dependencies like Streamlit, Selenium, and BeautifulSoup4.
### 2: Environment Setup:
* Set up a Python vertual environment for the project.
* Install dependencies: streamlit, Selenium, pyppeteer, beautifulsoup4, spacy, pandas ... .
* Download chrome driver for selemium to solve problem of complex platfrom scraping.
## Phase 2: Interface Design Using Streamlit

### 1: Set Up Streamlit UI:   
* A simple, interactive web interface is created using Streamlit, allowing users to input a URL and select specific options for content extraction and Named Entity Recognition (NER).
#### 2: User Feedback and Loading Indicators:
* Use Streamlit’s spinner to show a loading indicator during data extraction.
* Add feedback messages for successful data extraction or errors.

### 3: File Format Selection:
* Implement a drop-down menu to allow users to select the download format (CSV, PDF).
## Phase 3: API Key Creation
* Integration with the Groq platform to create an API key for accessing the Llama3 model. This step involves setting up a secure connection to enhance the app's processing capabilities.
## Phase 4: Content Scraping
* Utilizing Selenium for automated browsing and to retrieve dynamic web content.File Format Selection:
* The collected webpage data is then parsed using BeautifulSoup4 to clean and format the extracted content.
## Phase 5: Content Parsing
* The scraped data undergoes a cleaning process to ensure that it is structured and ready for analysis. This includes removing unnecessary whitespace and organizing the text for optimal processing (HTML Tag).
## Phase 6: LLM Processing
### 1: Model Setup Using API:
* Establish a connection to Llama3 through Groq's API, ensuring authentication using an API key. This setup prepares the app to send and receive data securely and efficiently.
### 2: Web Content Sent to Llama3:
* The content scraped from the web is passed to Llama3 through the API call, along with a prompt. This enables the model to process the content and extract the information needed by the user, such as Named Entity Recognition (NER).
### 3: Prompt Sent to Llama3:
* The user inputs a prompt, such as a request for Named Entity Recognition (NER), which is then sent to Llama3 along with the cleaned web content. This prompt guides the model to analyze the content and extract the specific information the user needs, such as identifying names, organizations, or other key entities.
* The refined content is passed to the Llama3 model via Groq's API. The model processes the content and extracts meaningful information based on specific prompts or questions.
## Phase 7:Data Export and Download Functionality
### 1: CSV Export:
* Convert the structured data (DataFrame) to CSV format.
* Create a Streamlit download button for the CSV file.
### 2: TEXT Export:
* Convert the data into Data Frame  and then to Text Format using .
* Ensure the Text format  is downloadable with a Streamlit download button.
## Phase 8: Testing and Debugging
### 1: Test the App on Different URLs:
* Test various website structures to ensure the scraper can handle different layouts.
### 2: Validate Output Formats:
* Ensure CSV and TEXT files download correctly and are formatted properly.
### 3: User Error Handling:
* Test for invalid URLs, network errors, and unsupported formats.
## Phase 9: Deployment and Documentation : ==> not finished yet !!
### 1: Deploy the App: 
* Deploy the app on a platform like Streamlit Cloud, Heroku, or any cloud service that supports Streamlit.
### 2: Documentation:
* Write documentation explaining the app’s purpose, features, and how to use it.
* Include setup instructions for others to install and run the app.
### 3: User Guide:
* Provide a guide for input requirements (valid URL formats, entity types) and supported file formats.
* This is link for deployment : ==>  https://web-app-scraping.streamlit.app
* Link Video demo :  https://github.com/Ismailnajib/Web_App_Scraping/blob/main/Video_demo.mp4
## Phase 10: Actual Problems
### 1: Deployment Issues:
* Chromedriver Problem: Description: The app relies on Chromedriver for web scraping tasks. However, during deployment, the Chromedriver cannot run directly on the Github Cloud platforms.
* Impact: This prevents the app from executing scraping tasks as expected.
* We are trying to solve the problem using different libraries for scraping.
* If the problem persists, our next step is to use a Docker container to see if it can resolve the issue.
  //
  //
![Screenshot (4)](https://github.com/user-attachments/assets/2cedb44f-cec1-467c-9345-f1ace9216cda)

  
