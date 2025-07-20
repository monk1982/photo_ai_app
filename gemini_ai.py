import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

def setup_page():
    st.header("📸 ĐẶT MỘT CÂU HỎI VỀ BỨC ẢNH CỦA BẠN.", anchor=False, divider="blue")
    st.sidebar.header("Hướng dẫn", divider="rainbow")
    st.sidebar.write("1. Chụp ảnh")
    st.sidebar.write("2. Đặt câu hỏi về bức ảnh")
    hide_menu_style =   """
                        <style>
                        #MainMenu {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

def gemini_ai():
    """
    1. Setup page
    2. Ask user to take a picture
    3. Submit to MLLM with a prompt
    4. Display response

    Returns
    -------
    None.
    """

    setup_page()
    enable = st.checkbox("Bật camera")
    camera_image = st.camera_input("Chụp ảnh",label_visibility="collapsed", disabled=not enable)
    if camera_image is not None:
        img = Image.open(camera_image)
        quest = st.text_input("Viết câu hỏi của bạn về bức ảnh","")
        if quest:
            client = genai.GenerativeModel(model_name='gemini-2.5-flash')
            response = client.generate_content([quest, img],
                                                generation_config= genai.types.GenerationConfig(temperature=2.0))
            response.resolve()
            st.markdown(response.text)

# Main codes run app    
GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')        
genai.configure(api_key= GOOGLE_API_KEY)
gemini_ai()
