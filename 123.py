import streamlit as st
st.write('我們的組名: 隨便啦 先孤輪')

confirm_input=st.button('圖片上傳')

if confirm_input:
  i=st.flim_input('圖片上傳')
