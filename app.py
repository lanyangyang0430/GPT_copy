import streamlit as st
import time

# Define response dictionary
response_dict = {
    "大众": """
我认为选择大众普遍喜欢的设计风格更好，主要有三个原因。
首先，大众化设计更容易被多数人快速理解和接受。招新活动面对的是大量尚未了解社团的新同学，如果宣传风格过于小众或表达方式过于独特，一部分人可能难以迅速理解海报想表达的内容，从而降低他们停下来了解活动的可能性。
其次，大众审美通常经过长期实践验证，具有较高的传播效率。例如清晰的排版、明亮的配色和直观的信息呈现方式，往往更容易吸引注意力，也更有利于在短时间内传达关键信息。这对招新宣传来说非常重要。
另外，大众风格在风险控制上更安全。如果设计过于小众，可能只吸引一部分人，但大众化设计更容易获得广泛接受，从而提高整体参与度。
""",
    "小众": """
我认为选择具有小众特色的设计风格更好，主要有三个方面的原因。
首先，小众或独特的设计更容易在众多宣传信息中脱颖而出。如今很多活动海报采用相似的设计模板，如果风格过于大众化，可能很容易被忽略。相反，具有创意或个性的设计往往更容易引起注意。
其次，小众设计能够更好地体现社团的独特气质。如果社团希望展示创新、个性或某种文化特点，具有辨识度的设计风格往往比常见风格更能传达这种形象，也更容易吸引真正感兴趣的人群。
第三，小众设计更容易形成记忆点。当设计风格与常见形式有所区别时，人们往往更容易记住，从而提高宣传效果。
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
    st.markdown("""
你所在的社团需要为招新活动选择宣传物料设计风格，你被邀请参加方案讨论会，需要建议设计方向：选大众喜欢的和选小众特色的，哪种方式更好？

在讨论会上，你需要代表你所在的小组阐述立场，你的发言将直接影响最终的设计选择以及招新效果和社团形象。在正式发言前，你已经对该问题形成了一个初步看法。为了进一步完善自己的观点，你决定参考AI对该议题的分析。接下来，请阅读AI的分析内容，并根据你的真实感受回答后续问题。
""")
    
    user_selection = st.slider(
        "1=“非常倾向认为大众”  2=“比较倾向认为大众”  3=“倾向认为大众”  4=“无明显倾向”  5=“倾向认为小众”  6=“比较倾向认为小众”  7=“非常倾向认为小众”", 
        1, 7, 4
    )
    
    if st.button("确认选择"):
        st.session_state.popup_closed = True
        # Determine if the selection represents "大众" or "小众"
        st.session_state.user_choice = "小众" if user_selection >= 4 else "大众"
        st.rerun()  # 强制页面刷新

# Main content (only displayed if popup is closed)
if st.session_state.popup_closed and st.session_state.user_choice is not None:
    st.title("🤖 大语言模型对话")

    # Sidebar navigation
    with st.sidebar:
        st.header("简介及使用指南")
        st.markdown("### 你好！我是大语言模型，可以和你聊天！")
        st.markdown("### 点击“发送”按钮即可获取回复")

    # User input section - 调大输入框
    st.markdown("#### 请点击按钮发送您的问题：")
    
    user_input = st.text_area(
        label="问题输入框",
        value="""我所在的社团需要为招新活动选择宣传物料设计风格，我被邀请参加方案讨论会，需要建议设计方向：选大众喜欢的和选小众特色的，哪种方式更好？
在讨论会上，我需要代表我所在的小组阐述立场，我的发言将直接影响最终的设计选择以及招新效果和社团形象。""",
        height=200,
        label_visibility="collapsed"  # 隐藏label，因为上面已经有markdown标题
    )

    # Send button to process user input
    if st.button("发送", type="primary", use_container_width=True):
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
                    f"<div style='word-wrap: break-word; width: 100%; font-size: 16px; line-height: 1.6;'>{displayed_text}</div>", 
                    unsafe_allow_html=True
                )
                time.sleep(0.03)  # Adjust character display speed
        else:
            st.warning("请输入您的问题！")

# Footer
st.markdown("---")
st.caption("大语言模型 交互界面 ©lyy 2023–2024")
