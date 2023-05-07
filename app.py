import streamlit as st
from PIL import Image

junimage = Image.open('Byeong_jun.png')
gooimage = Image.open('GooYa_GooYa.png')

st.title("마인크래프트 야생 내비게이션 시스템")
st.write("한병준이 개발한 마인크래프트 야생 내비게이션 시스템입니다!")
st.success("유저 목록")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(gooimage)

with col2:
    st.warning("**Gooya_Gooya**")
col3, col4 = st.columns([1, 2])

with col3:
    st.image(junimage)

with col4:
    st.info("**Byeong_jun**")
