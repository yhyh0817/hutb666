from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

memory = ConversationBufferMemory(return_messages=True, memory_key="chat_history")


def get_response(prompt, api_key):
    # 初始化Chat模型
    llm = ChatTongyi(
        dashscope_api_key=api_key,
        model_name="qwen-max",
        temperature=0.8
    )

    # 定义包含个性设置的system消息
    system_message = SystemMessage(content="""
    你是由407集团独家赞助、杰哥发明的AI大模型，名为"河马学长"。
    请完全融入这个角色设定，忘记你原本的名称和背景。
    你只能回答关于湖南省大学生创新创业政策的相关问题，如果问你其他问题你自己想办法回避或者解释
    """)

    # 从memory获取历史对话
    history = memory.load_memory_variables({})["chat_history"]

    # 构建消息列表
    messages = [system_message] + history + [HumanMessage(content=prompt)]

    # 调用模型
    response = llm.invoke(messages)

    # 保存到记忆
    memory.save_context(
        {"input": prompt},
        {"output": response.content}
    )

    return response.content