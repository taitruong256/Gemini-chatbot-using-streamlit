import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv 
import os 


load_dotenv()
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

if prompt := st.chat_input('Nhập câu hỏi: '):
    with st.chat_message('user'):
        st.markdown(prompt)
    
    response = model.generate_content(prompt)
    reply = response.text
    
    with st.chat_message('asistant'):
        st.markdown(reply)