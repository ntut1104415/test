import streamlit as st
st.write('我們的組名: 隨便啦 先孤輪')

confirm_input=st.button('圖片上傳')

if confirm_input:
  i=get_image_files('https://github.com/ntut1104415/test123/blob/c54545f1dcb7cb576177315928546f347cb2eb93/car1.jpg')
