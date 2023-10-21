import streamlit as st
import pandas as pd

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os
import markdown

def _max_width_():
    max_width_str = "max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .block-container {{
        {max_width_str}
        }}
    .custom-widget {{
        display: grid;
        border: 1px solid black;
        padding: 12px;
        border-radius: 5%;
        color: #003366;
        margin-bottom: 5px;
        min-height: 251.56px;
        align-items: center;
    }}
    .row-widget.stCheckbox {{
        display: grid;
        justify-content: center;
        align-items: center;
        border: solid 2px black;
        border-radius: 3%;
        height: 50px;
        background-color: #DF1B88;
        color: #FFFFFF;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

_max_width_()



def send_email(to_emails = 'testEmail@gprof.com',
               subject='Test Email: Please respond',
               message = '<strong>This should work</strong> even without Bolding'):
  message = Mail(
      from_email='anoushka1001@gprof.com',
      to_emails=to_emails,
      subject=subject,
      html_content=message)
  try:
      sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
      print("Completed successfully")
  except Exception as e:
      print(e)
      print("Did not succeed")


def get_conversation_summary(p, d):
    formatted_messages = [f"## {m['role']}:\n### {m['content']}\n\n" for m in st.session_state.messages]
    formatted_string="\n**********\n".join(formatted_messages)
    print(f"Formatted string is {formatted_string}")
    summary=f"""
### Hi {p}, {d}

###The student has requested your assistance. Can you please reach out to them asap? 
    
###thanks
    
###-Counsel
    
###Here is the conversation log: 
{formatted_string}
    """
    print(f"Summary is {summary}")
    html_summary=markdown.markdown(summary)
    print(f"HTML summary is {html_summary}")
    return html_summary

csv_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vSxN7ZYdU8BJ5GJ9MDFoUIeEcHgNLOZhVdMQaMUs0nKP_zgyGb6NAAYjJEofROV86O5kRwszJOEqI7U/pub?gid=0&single=true&output=csv'
df=pd.read_csv(csv_file)

num_rows=len(df)
st.markdown(f'# Meet our counselors')
#st.table(df)

for i in range(len(df)):
    with st.container():
        (col1,col2)=st.columns([7,3])
        row = df.iloc[i]
        p=row['Name']
        d=row['Credentials']
        de=row['Description']
        ur=row['url']
        em=row['Email']
        desc=f'## {p} \n### {d}\n {de}'
        col2.image(ur,use_column_width=True)
        col1.markdown(desc)
        if col2.button("Send Chat Summary",key=f'button{i}'):
            g=get_conversation_summary(p, d)
            send_email(em,'EducationALLY Chat Summary',g)
           #with st.sidebar.expander(f"Email message sent to {p}"):
               # st.markdown(f"To: {em}.\n Body: {g}")
            st.write(f"Chat summary sent to {p}")
        st.divider()
        