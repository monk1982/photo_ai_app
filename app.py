import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

def setup_page():
    st.header("📸 Ask a MLLM questions about your picture.", anchor=False, divider="blue")
    st.sidebar.header("About the app", divider="rainbow")
    st.sidebar.write("1. Take a photo")
    st.sidebar.write("2. Ask question about your photo")
    hide_menu_style =   """
                        <style>
                        #MainMenu {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
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

    camera_image = st.camera_input("Take a picture")
    if camera_image is not None:
        img = Image.open(camera_image)
        quest = st.text_input("Enter your question and hit return","")
        if quest is not None:
            client = genai.GenerativeModel(model_name='gemini-1.0-pro-vision-latest')
            response = client.generate_content([quest, img], generation_config= genai.types.GenerationConfig(temperature=2.0, max_output_tokens=300))
            response.resolve()
            st.markdown(response.text)

# Main codes run app    
if __name__=='__main__':
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY_NEW')
    genai.configure(api_key= GOOGLE_API_KEY)
    main()
