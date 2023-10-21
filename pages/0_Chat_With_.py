# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

import openai
import streamlit as st

openai.api_key = st.secrets['OPENAI_API_KEY']

st.markdown("# Chat with __")
avatars={"system":"💻🧠","user":"🧑‍💼","assistant":"🎓"}

SYSTEM_PROMPT = '''
You are a guidance counselor. Students come to you to get advice on college admissions. 
Before providing advice, you ask questions to provide the best advice and guidance to these students. 
'''
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content": SYSTEM_PROMPT})

for message in st.session_state.messages:
    avatar=avatars[message["role"]]
    if message["role"] != "system" : 
        with st.chat_message(message["role"], avatar = avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})