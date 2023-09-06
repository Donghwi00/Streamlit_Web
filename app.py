import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon="🎉",
    page_title="Test_Deploy",
    layout="wide"
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("Streamlit Test Page")
st.subheader("회원가입, 로그인")

st.write('# Test')
st.write('## 회원가입, 로그인')