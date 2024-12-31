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
st.title("About")
st.write("This is the About page where you can add details about the app, its purpose, and the creator.")
st.write("""
This app is a simple multi-page Streamlit app demonstrating how to organize content.
Streamlit allows us to create visually appealing and interactive applications quickly and easily.
""")
