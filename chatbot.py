import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv 
import os 


load_dotenv()
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

user_input = st.text_input("Nhập nội dung:")

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(user_input)
st.write(response.text)