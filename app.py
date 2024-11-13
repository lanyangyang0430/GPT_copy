import streamlit as st
import time

# Define response dictionary
response_dict = {
    "过程": """
我认为过程更重要。过程决定了我们如何应对挑战、如何成长和学习。在过程中，我们往往可以积累经验、发展技能并塑造自己的思维方式。通过反复探索和解决问题，我们不仅会提高自己的能力，还会发现新的方法和途径，这对个人发展至关重要。结果固然是衡量成功的标准，但它往往是一个瞬间的体现，而过程却是一个持续的积累，是实现真正长期价值和成就的基石。无论最终结果如何，过程中的投入和体验本身就是一种不可替代的成长。
""",
    "结果": """
我认为结果更重要。结果往往反映了事物所带来的实际影响和价值。例如，医生的成功不仅体现在他们诊断过程中的技术能力，还体现在他们能否治愈病人、提高患者的生活质量；工程师的工作不仅要体现在设计和实施的过程中，还必须通过最终的建筑物或产品质量来证明。如果过程再怎么努力，但没有实际的、有价值的成果，社会对个体的评价往往也会大打折扣。不管是时间、金钱还是人力资源，任何一种资源都有其有限性。结果往往会影响后续我们获取的各种资源和机会。
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
    st.write("### 您更倾向过程/结果哪个更重要？")
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
    user_input = st.text_input("请点击按钮发送您的问题：", value="您更倾向过程/结果哪个更重要？")

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
