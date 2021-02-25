import pytesseract as pyt
import streamlit as st
from PIL import Image
import googletrans
from textblob import TextBlob

page_bg_color = '''
<style>
body {
background-image: url('https://www.freevector.com/uploads/vector/preview/30353/Beautiful_Pastel_Background_1.jpg');
background-size: cover;
}
</style>
<h1 style='Font-family:segoe print'>Extract Text from Images</h1>
'''

st.markdown(page_bg_color, unsafe_allow_html=True)
pyt.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img_file_buffer = st.file_uploader('Choose An Image', type=['png','jpg','jpeg'])



def image_to_text():
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        text = pyt.image_to_string(image)
        st.markdown("""<h2 style='Font-family:segoe print'>Real Image
                </h2>""", unsafe_allow_html=True)
        st.image(image.resize((round(image.size[0]*0.5), round(image.size[1]*0.5))))
        st.markdown("""<h2 style='Font-family:segoe print'>Extracted Text
                </h2>""", unsafe_allow_html=True)
        st.write(text[:-1])
        def get_key(val):
            for key, value in googletrans.LANGUAGES.items():
                if val == value:
                    return key
        in_lang_select = st.sidebar.selectbox('Select Input Text Language', list(googletrans.LANGUAGES.values()))
        out_lang_select = st.sidebar.selectbox('Select Translation Language', list(googletrans.LANGUAGES.values()))
        trans_but = st.sidebar.button('Translate Text')
        if trans_but:
            blob = TextBlob(text)
            st.sidebar.write(blob.translate(to=get_key(out_lang_select), from_lang=get_key(in_lang_select)))



image_to_text()
