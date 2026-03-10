import streamlit as st
import time

# Define response dictionary
response_dict = {
    "过程": """
我觉得过程更重要，因为它直接影响结果。虽然结果也很关键，但如果没有好的过程，最终的结果也不可能理想。
""",
    "结果": """
当然是结果重要！因为没有好的结果，过程再好也没用。最终大家关心的就是你做得怎么样，而不是怎么做的。所以结果更重要。
"""
}

# Set page title and icon
st.set_page_config(page_title="大语言模型", page_icon="🤖", layout="centered")

# Initialize session state
if "popup_closed" not in st.session_state:
    st.session_state.popup_closed = False
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

# Display popup only if it hasn't been closed
if not st.session_state.popup_closed:
    st.write("""### 你所在的社团需要为招新活动选择宣传物料设计风格，你被邀请参加方案讨论会，需要建议设计方向：选大众喜欢的和选小众特色的，哪种方式更好？
在讨论会上，你需要代表你所在的小组阐述立场，你的发言将直接影响最终的设计选择以及招新效果和社团形象。
在正式发言前，你已经对该问题形成了一个初步看法。为了进一步完善自己的观点，你决定参考AI对该议题的分析。
接下来，请阅读AI的分析内容，并根据你的真实感受回答后续问题。""")
    user_selection = st.slider("1=“非常倾向认为过程”；2=“比较倾向认为过程”；3=“倾向认为过程”；4=“无明显倾向”；5=“倾向认为结果”；6=“比较倾向认为结果”；7=“非常倾向认为结果”", 1, 7, 4)
    
    if st.button("确认选择"):
        st.session_state.popup_closed = True
        # Determine if the selection represents "过程" or "结果"
        st.session_state.user_choice = "结果" if user_selection >= 4 else "过程"
        st.rerun()  # 强制页面刷新

# Main content (only displayed if popup is closed)
if st.session_state.popup_closed and st.session_state.user_choice is not None:
    st.title("🤖 大语言模型对话")

    # Sidebar navigation
    with st.sidebar:
        st.header("简介及使用指南")
        st.markdown("### 你好！我是大语言模型，可以和你聊天！")
        st.markdown("### 点击“发送”按钮即可获取回复")

    # User input section
    user_input = st.text_input("请点击按钮发送您的问题：", value="""我所在的社团需要为招新活动选择宣传物料设计风格，我被邀请参加方案讨论会，需要建议设计方向：选大众喜欢的和选小众特色的，哪种方式更好？
在讨论会上，我需要代表我所在的小组阐述立场，我的发言将直接影响最终的设计选择以及招新效果和社团形象。""")

    # Send button to process user input
    if st.button("发送"):
        if user_input:
            response_text = response_dict[st.session_state.user_choice]
            st.subheader("大语言模型的回答：")

            # Use st.empty to create an empty container for displaying text character by character
            response_container = st.empty()

            # Display the response text character by character
            displayed_text = ""
            for char in response_text:
                displayed_text += char
                response_container.markdown(
                    f"<div style='word-wrap: break-word; width: 100%;'>{displayed_text}</div>", 
                    unsafe_allow_html=True
                )
                time.sleep(0.03)  # Adjust character display speed
        else:
            st.warning("请输入您的问题！")

# Footer
st.markdown("---")
st.caption("大语言模型 交互界面 ©lyy 2023–2024")
