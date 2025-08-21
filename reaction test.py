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
if "fail" not in st.session_state:
    st.session_state.fail = False
if "status" not in st.session_state:
    st.session_state.status = "idle"  # idle / waiting / ready / fail / done


def start_test():
    wait_time = random.uniform(2, 5)
    st.session_state.target_time = time.time() + wait_time
    st.session_state.reaction_time = None
    st.session_state.show_click_button = True
    st.session_state.fail = False
    st.session_state.status = "waiting"


def record_reaction():
    if st.session_state.status == "ready":  # 정상 클릭
        st.session_state.reaction_time = time.time() - st.session_state.start_time
        st.session_state.status = "done"
    elif st.session_state.status == "waiting":  # 너무 일찍 클릭
        st.session_state.fail = True
        st.session_state.status = "fail"


# 시작 버튼
if st.button("🟢 테스트 시작"):
    start_test()

# 상태 갱신
if st.session_state.status == "waiting":
    if time.time() >= st.session_state.target_time:
        st.session_state.start_time = time.time()
        st.session_state.status = "ready"
        st.rerun()

# 안내 메시지
if st.session_state.status == "idle":
    st.info("테스트를 시작하려면 위 버튼을 누르세요.")
elif st.session_state.status == "waiting":
    st.warning("⏳ 준비 중... 버튼이 나타나면 바로 눌러야 합니다!")
elif st.session_state.status == "ready":
    st.success("🚨 지금 클릭하세요!")
elif st.session_state.status == "fail":
    st.error("❌ 너무 빨랐습니다! 버튼이 나타난 후에 클릭하세요.")
elif st.session_state.status == "done":
    st.success(f"⏱ 반응 속도: {st.session_state.reaction_time:.3f}초")

# 클릭 버튼 (위치 고정)
if st.session_state.show_click_button:
    if st.button("👆 클릭 버튼", key="click_btn"):
        record_reaction()
        st.rerun()

# 다시 시도
if st.session_state.status in ["fail", "done"]:
    if st.button("🔁 다시 시도"):
        st.session_state.status = "idle"
        st.session_state.show_click_button = False
        st.session_state.reaction_time = None
        st.session_state.target_time = 0
        st.session_state.fail = False
