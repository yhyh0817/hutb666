# app.py
import streamlit as st
from tool import get_response  # 从 tool.py 导入 get_response

if "message" not in st.session_state:
    st.session_state["message"] = []

st.title("河马学长AI 2.0抢先版")
st.divider()

prompt = st.chat_input("请输入问题：")
if prompt:
    try:
        st.session_state["message"].append({"role": "user", "content": prompt})
        for msg in st.session_state['message']:
            st.chat_message(msg['role']).markdown(msg['content'])
        with st.spinner("思考ing......"):
            res = get_response(prompt)  # 调用 get_response 函数
            st.session_state['message'].append({"role": "assistant", "content": res})
            st.chat_message("assistant").markdown(res)

    except Exception as e:
        st.error(f"应用运行时出错：{e}")