import streamlit as st
import time
import random

st.title("🧠 반응 속도 테스트")

# 세션 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "waiting" not in st.session_state:
    st.session_state.waiting = False
if "ready" not in st.session_state:
    st.session_state.ready = False
if "reaction_time" not in st.session_state:
    st.session_state.reaction_time = None


def start_test():
    st.session_state.waiting = True
    st.session_state.ready = False
    st.session_state.reaction_time = None
    wait_time = random.uniform(2, 5)  # 2~5초 랜덤 대기
    time.sleep(wait_time)
    st.session_state.start_time = time.time()
    st.session_state.waiting = False
    st.session_state.ready = True


def record_reaction():
    if st.session_state.ready:
        reaction = time.time() - st.session_state.start_time
        st.session_state.reaction_time = reaction
        st.session_state.ready = False


# UI 구성
if not st.session_state.waiting and not st.session_state.ready:
    if st.button("🟢 테스트 시작"):
        start_test()

elif st.session_state.waiting:
    st.write("⏳ 기다리는 중... (곧 버튼이 나타납니다)")

elif st.session_state.ready:
    if st.button("🚨 지금 클릭!"):
        record_reaction()

if st.session_state.reaction_time is not None:
    st.success(f"⏱ 반응 속도: {st.session_state.reaction_time:.3f}초")
    if st.button("🔁 다시 시도"):
        st.session_state.ready = False
        st.session_state.reaction_time = None











