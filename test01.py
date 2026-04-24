from tool import get_response
import streamlit as st

st.set_page_config(
    page_title="河马学长AI 2.0抢先版",
    page_icon="🦛"
)

st.title("河马学长AI 2.0抢先版")
st.divider()

if "message" not in st.session_state:
    st.session_state["message"] = []

# 显示历史聊天记录
for msg in st.session_state["message"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("请输入问题：")

if prompt:
    st.session_state["message"].append({
        "role": "user",
        "content": prompt
    })

    st.chat_message("user").markdown(prompt)

    with st.spinner("思考ing......"):
        res = get_response(
            prompt=prompt,
            history=st.session_state["message"][:-1]
        )

    st.session_state["message"].append({
        "role": "assistant",
        "content": res
    })

    st.chat_message("assistant").markdown(res)