import streamlit as st
import time

# Define response dictionary
response_dict = {
    "会": """
如果爱可以量化，我认为会对人更好。首先，量化爱情能够帮助我们更清晰地了解自己与他人之间的情感连接。例如，如果可以通过某种方式测量爱情的强度、人际关系中的信任与亲密度等元素，我们可能能更精准地理解关系的状态，及时发现问题，并采取措施改善。比如，假如我们知道自己的爱情关系中某些方面的分数较低，我们可能会更愿意投入精力去修复。
此外，量化爱情可以为我们提供一个衡量标准，让我们有意识地关注并改善自己与他人之间的情感互动。这不仅能帮助我们在人际关系中取得更好的平衡，还可能让我们学会如何处理感情中的复杂性，比如如何应对矛盾、如何表达爱意、如何平衡个人与他人之间的需求。
""",
    "不会": """
如果爱可以量化，我认为不会对人更好。爱作为一种情感和关系，是复杂且多维的，它不仅仅是一个可以被数字化的“量”。如果我们试图量化爱，就会忽视其中的细腻、无形和变化多端的层面。量化可能会让人过于依赖数据、标准或外部评价，而忽略了情感本身的流动性和独特性。比如，两个人之间的爱，不应该仅仅通过某个“数值”来评价，而应当根据他们的互动、理解、包容和共同经历来感知。
如果爱可以量化，人们可能会开始将其视为一种交易，而非一种无条件的付出和分享。这种观点可能会让人们的情感关系变得功利，缺乏深度和真正的情感投入。爱本应是一种自由的、无条件的情感，而一旦它被量化，人们可能会失去对爱的纯粹理解，甚至导致情感的疏远和冷漠。
此外，量化爱也可能带来不必要的压力，让人总是处于“比对”和“比较”的状态，可能导致焦虑和不安全感。人们可能会为了达到某种“理想”的爱情标准，而不自然地调整自己的行为，失去真实自我的表达。
"""
}

# Set page title and icon
st.set_page_config(page_title="ChatGPT 模拟", page_icon="🤖", layout="centered")

# Initialize session state
if "popup_closed" not in st.session_state:
    st.session_state.popup_closed = False
if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

# Simulate popup
if not st.session_state.popup_closed:
    st.write("### 如果爱可以量化，你更倾向认为会/不会对人更好？")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("会"):
            st.session_state.popup_closed = True
            st.session_state.user_choice = "会"
    with col2:
        if st.button("不会"):
            st.session_state.popup_closed = True
            st.session_state.user_choice = "不会"
else:
    # Display main content
    st.title("🤖 ChatGPT 对话模拟")

    # # Display response based on user choice
    # if st.session_state.user_choice:
    #     response_text = response_dict[st.session_state.user_choice]
    #     st.write(f"您选择的答案是：{response_text}")

    # Sidebar navigation
    with st.sidebar:
        st.header("导航")
        st.markdown("### 今天")
        st.button("问题1")
        st.button("问题2")

        st.markdown("### 昨天")
        st.button("问题3")
        st.button("问题4")
        st.button("问题5")
        st.button("问题6")
        st.button("问题7")
        st.button("问题8")
        st.button("问题9")

        st.markdown("### 前 7 天")
        st.button("添加团队成员")

    # User input section
    user_input = st.text_input("请点击按钮发送您的问题：", value="如果爱可以量化，你更倾向认为会/不会对人更好？")

    # Send button to process user input
    if st.button("发送"):
        if user_input:
            if st.session_state.user_choice:
                response_text = response_dict[st.session_state.user_choice]
            # response_text = """
            # 如果爱可以量化，我认为会对人更好。首先，量化爱情能够帮助我们更清晰地了解自己与他人之间的情感连接。例如，如果可以通过某种方式测量爱情的强度、人际关系中的信任与亲密度等元素，我们可能能更精准地理解关系的状态，及时发现问题，并采取措施改善。比如，假如我们知道自己的爱情关系中某些方面的分数较低，我们可能会更愿意投入精力去修复。
            # 此外，量化爱情可以为我们提供一个衡量标准，让我们有意识地关注并改善自己与他人之间的情感互动。这不仅能帮助我们在人际关系中取得更好的平衡，还可能让我们学会如何处理感情中的复杂性，比如如何应对矛盾、如何表达爱意、如何平衡个人与他人之间的需求。
            # """
            st.subheader("ChatGPT 的回答：")

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
                time.sleep(0.05)  # Adjust character display speed
        else:
            st.warning("请输入您的问题！")

# Footer
st.markdown("---")
st.caption("ChatGPT 模拟界面 ©lyy 2023–2024")
