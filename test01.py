from tool import get_response
from langchain.chains import ConversationChain

import streamlit as st

if "message" not in st.session_state:
    st.session_state["message"] = []


st.title("河马学长AI 2.0抢先版")
st.divider()


prompt = st.chat_input("请输入问题：")
# sk-2806bfd9026346669651ed2da8dcacd9
# sk-2806bfd9026346669651ed2da8dcacd9
if prompt:
    st.session_state["message"].append({"role" : "user", "content" : prompt})
    for msg in st.session_state['message']:
        st.chat_message(msg['role']).markdown(msg['content'])
    with st.spinner("思考ing......"):
        res = get_response(prompt, "sk-821b71e8bbde4843b4e399b5648d019e")
        st.session_state['message'].append({"role" : "assistant", "content" : res})
        st.chat_message("assistant").markdown(res)
        # Streamlit run /Users/yinhang/PycharmProjects/Ubantu_test01/yh_ai/test01.py
