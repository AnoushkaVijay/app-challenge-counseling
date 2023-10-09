# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import streamlit as st
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(to_email = 'anoushka1001@gmail.com', message = '<strong>and easy to do anywhere, even with Python</strong>'):
  message = Mail(
      from_email='anoushka1001@gprof.com',
      to_emails='anoushka1001@gmail.com',
      subject='Msg 3: Contact Counselor',
      html_content='<strong>and easy to do anywhere, even with Python</strong>')
  try:
      sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
      print("Completed successfully")
  except Exception as e:
      print(e.message)
      print("Did not succeed")
if st.button('send email'):
   send_email()
