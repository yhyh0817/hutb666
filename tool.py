# tool.py
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

memory = ConversationBufferMemory(return_messages=True, memory_key="chat_history")

def get_response(prompt):
    try:
        # 获取API密钥
        api_key = os.getenv("dashscope_api_key")
        if not api_key:
            return "API 密钥未找到，请确保正确配置密钥。"  # 提示而不是抛出异常

        # 初始化Chat模型
        try:
            llm = ChatTongyi(
                dashscope_api_key=api_key,
                model_name="qwen-max",
                temperature=0.8
            )
        except ImportError as e:
            return f"模型初始化失败：{e}"  # 返回错误信息而不是抛出异常
        except Exception as e:
            return f"初始化 ChatTongyi 模型时出现其他错误：{e}"

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
        try:
            response = llm.invoke(messages)
        except Exception as e:
            return f"调用模型时出现错误：{e}"  # 返回错误信息而不是抛出异常

        # 保存到记忆
        memory.save_context(
            {"input": prompt},
            {"output": response.content}
        )

        return response.content

    except Exception as e:
        return f"发生了一个未知错误：{e}"  # 捕获其他未知错误并返回