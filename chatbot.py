import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv 
import os 


load_dotenv()
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

if 'messages' not in st.session_state:
    st.session_state.messages = [] 
    
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

if prompt := st.chat_input('Nhập câu hỏi: '):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message('user'):
        st.markdown(prompt)
        
    history_chat = ''
    for msg in st.session_state.messages:
        history_chat += f'{msg['role']}: {msg['content']} \n'
    
    response = model.generate_content(history_chat)
    reply = response.text
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    with st.chat_message('asistant'):
        st.markdown(reply)