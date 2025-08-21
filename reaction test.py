import streamlit as st
import time
import random

st.title("🧠 반응 속도 테스트")

# 세션 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "show_click_button" not in st.session_state:
    st.session_state.show_click_button = False
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = None
if "target_time" not in st.session_state:
    st.session_state.target_time = 0


# 테스트 시작 함수
def start_test():
    wait_time = random.uniform(2, 5)
    st.session_state.target_time = time.time() + wait_time
    st.session_state.reaction_time = None
    st.session_state.show_click_button = False


# 반응 시간 기록 함수
def record_reaction():
    st.session_state.reaction_time = time.time() - st.session_state.start_time
    st.session_state.show_click_button = False


# 상태에 따른 UI 표시
if st.button("🟢 테스트 시작"):
    start_test()

# 대기 상태 처리
if st.session_state.target_time > 0 and not st.session_state.show_click_button:
    current_time = time.time()
    if current_time >= st.session_state.target_time:
        st.session_state.start_time = current_time
        st.session_state.show_click_button = True
    else:
        st.write("⏳ 준비 중...")

# 클릭 버튼 표시
if st.session_state.show_click_button:
    if st.button("🚨 지금 클릭!"):
        record_reaction()

# 결과 표시
if st.session_state.reaction_time is not None:
    st.success(f"⏱ 반응 속도: {st.session_state.reaction_time:.3f}초")
    if st.button("🔁 다시 시도"):
        st.session_state.reaction_time = None
        st.session_state.target_time = 0
        st.session_state.show_click_button = False
