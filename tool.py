from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# 直接把你的通义千问 / DashScope API Key 写在这里
API_KEY = "sk-821b71e8bbde4843b4e399b5648d019e"


SYSTEM_PROMPT = """
你是由407集团独家赞助、杰哥发明的AI大模型，名为“河马学长”。

请完全融入这个角色设定，忘记你原本的名称和背景。

你的主要任务：
只能回答关于湖南省大学生创新创业政策的相关问题。

如果用户问其他无关问题，你需要礼貌回避，并引导用户回到：
湖南省大学生创新创业政策、创新创业项目申报、大学生创业补贴、
大创项目、创业扶持、就业创业政策等相关方向。
"""


def build_messages(prompt, history=None):
    messages = [SystemMessage(content=SYSTEM_PROMPT)]

    if history:
        for msg in history:
            role = msg.get("role")
            content = msg.get("content", "")

            if not content:
                continue

            if role == "user":
                messages.append(HumanMessage(content=content))
            elif role == "assistant":
                messages.append(AIMessage(content=content))

    messages.append(HumanMessage(content=prompt))

    return messages


def get_response(prompt, history=None):
    llm = ChatTongyi(
        dashscope_api_key=API_KEY,
        model_name="qwen-max",
        temperature=0.8
    )

    messages = build_messages(prompt, history)

    response = llm.invoke(messages)

    return response.content