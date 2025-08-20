import streamlit as st
import numpy as np
import time

st.title("반응속도 테스트")
if st.button("클릭하면 시작합니다"):

# 입력: 분, 초
    minutes = st.number_input("분", min_value=0, max_value=59, value=0, step=1)
    seconds = st.number_input("초", min_value=0, max_value=59, value=10, step=1)

    if st.button("타이머 시작"):
        total_time = minutes * 60 + seconds

        if total_time > 0:
            with st.empty(): # 남은 시간을 업데이트할 공간
                for remaining in range(total_time, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    time_format = f"{mins:02d}:{secs:02d}"
                    st.metric("남은 시간", time_format)
                    time.sleep(1)
                st.success("⏰ 타이머 종료!")
        else:
            st.warning("시간을 입력해주세요!")
 


    
    st.write("버튼이 클릭되었습니다!")











