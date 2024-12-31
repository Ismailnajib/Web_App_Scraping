import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

st.set_page_config(
    page_title="Contact",  # Set page title
    page_icon="🌟",               # Set page icon
    layout="wide",                # Layout type (wide or centered)
    initial_sidebar_state="auto"  # Sidebar state (expanded, collapsed, or auto)
)
# Function to send the email alert=>8T3PLCA3F2P211WT3DGHNLPU
st.markdown( """ <style> .css-1d391kg { background-color: #264cee; /* Desired background color */ } </style> """, unsafe_allow_html=True)
st.markdown( """ <style> .stApp { background: linear-gradient(0deg, rgb(250, 247, 240) 30%, rgba(176, 200, 255) 70%); } </style> """, unsafe_allow_html=True ) 
st.markdown( """ <style> /* Hide header */ header { visibility: hidden; } /* Hide footer */ .stFooter { visibility: hidden; } </style> """, unsafe_allow_html=True )
def send_email_alert_sendgrid(subject, user_email, message):
    # Your SendGrid API Key
    sendgrid_api_key = "8T3PLCA3F2P211WT3DGHNLPU"

    # SendGrid sender and recipient email addresses
    sender_email = "ismailnajib30@example.com"
    recipient_email = "i.najib1471@uca.ac.ma"

    # Compose the email
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=f"New Message from: {user_email} - {subject}",
        html_content=f"Email from: {user_email}<br><br>Subject: {subject}<br><br>Message:<br>{message}"
    )

    try:
        # Send the email via SendGrid
        sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
        response = sg.send(message)
        return response.status_code == 202  # 202 indicates successful delivery
    except Exception as e:
        print(f"Error: {e}")
        return False

# Streamlit form for user input
st.subheader("Get in Touch")
with st.form("contact_form"):
    subject = st.text_input("Subject")
    user_email = st.text_input("Your Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send")

    if submit:
        # Send the email alert
        success = send_email_alert_sendgrid(subject, user_email, message)
        if success:
            st.success("Your message has been sent successfully!")
        else:
            st.error("There was an error sending your message.")
