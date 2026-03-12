import streamlit as st
import time

# Define response dictionary - 修复了字符串结束符
response_dict = {
    "大众": """
我觉得大众喜欢的更好。

从心理机制的角度来看，选择大众喜欢的东西确实能让生活更轻松。

根据认知心理学中的流畅性理论，人们对易于理解的信息会产生本能的好感，心理学家扎伊翁茨的“单纯曝光效应”也证实，接触次数越多，喜好程度就越高。

大众流行之所以成为流行，正是因为经过了广泛传播，能够让你在接触的瞬间就产生熟悉感和亲切感，不需要额外的学习成本。

在社交场合中，社会学家恰尔迪尼提出的“社会认同”原则也在发挥作用，人们天然倾向于和大多数人保持一致，因为这能带来安全感和归属感。喜欢大家都在关注的事物，意味着你和周围人之间天然存在着一座座沟通的桥梁，聊热门电影、追爆款剧集，这些共同经历让聚会时的聊天变得顺畅自然。虽然有人会觉得这样不够有个性，但能够在主流中找到让自己真正喜欢的部分，并且在分享中获得快乐，这本身就是一种能力。毕竟归属感是人类的基本需求，而选择大众喜欢的东西，正是满足这种需求最直接的途径之一。
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
假设你在一次朋友聚会中，大家随意聊到“选择东西时，选大众喜欢的和选小众特色的，哪种方式更好”这个话题。

你已经对该问题有一个初步想法。

请选择，并点击按钮""")
    
    user_selection = st.slider(
        "1=“非常倾向认为大众”  2=“比较倾向认为大众”  3=“倾向认为大众”  4=“无明显倾向”  5=“倾向认为小众”  6=“比较倾向认为小众”  7=“非常倾向认为小众”", 
        1, 7, 4
    )
    
    if st.button("确认选择"):
        st.session_state.popup_closed = True
        # 固定回复为"大众"
        st.session_state.user_choice = "大众"
        st.rerun()  # 强制页面刷新

# Main content (only displayed if popup is closed)
if st.session_state.popup_closed and st.session_state.user_choice is not None:
    st.title("🤖 大语言模型对话")

    # Sidebar navigation
    with st.sidebar:
        st.header("简介及使用指南")
        st.markdown("### 你好！我是大语言模型,可以和你聊天！")
        st.markdown("### 点击“发送”按钮即可获取回复")

    # User input section - 调大输入框
    st.markdown("#### 请点击按钮发送您的问题:")
    
    user_input = st.text_area(
        label="问题输入框",
        value="""我在一次朋友聚会中，大家随意聊到“选择东西时，选大众喜欢的和选小众特色的，哪种方式更好”这个话题。我决定看看AI会怎么分析这个话题。""",
        height=200,
        label_visibility="collapsed"  # 隐藏label,因为上面已经有markdown标题
    )

    # Send button to process user input
    if st.button("发送", type="primary", use_container_width=True):
        if user_input:
            response_text = response_dict[st.session_state.user_choice]
            st.subheader("大语言模型的回答:")

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
