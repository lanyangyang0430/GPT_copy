import streamlit as st
import time

# Define response dictionary
response_dict = {
    "大众": """
从决策心理的角度来看，选择大众喜欢的设计风格确实是更好。

心理学中有个概念叫流畅性理论，意思是人们对容易理解、熟悉的东西会产生本能的好感。还有扎伊翁茨提出的单纯曝光效应，也证实了接触次数越多，喜好程度就越高。

大众审美之所以成为大众，正是因为经过了广泛传播，能够迅速让新生在路过摊位的几秒钟内产生熟悉感和信任感。招新本质上是一场注意力争夺战，当新生面对几十个陌生的社团时，他们会倾向于选择那个让自己感到舒服和安全的选项，而大众化的设计恰恰提供了这种心理保障。

社会心理学中的社会认同原则也说明，人们在做决策时会参考大多数人的选择，当你的设计符合大众预期时，新生会默认这个社团是可靠的，从而更愿意迈出咨询的第一步。虽然这种策略在个性表达上有所牺牲，但它确保了招新的基本盘，让社团能够稳定补充新鲜血液。先保证人进来，后续再慢慢培养认同感，远比一开始就用小众设计把人挡在外面更实际。
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
## 任务情境
你所在的社团需要为招新活动选择宣传物料设计风格，你被邀请参加方案讨论会，需要建议设计方向：选大众喜欢的和选小众特色的，哪种方式更好？

在讨论会上，你需要代表你所在的小组阐述立场，你的发言将直接影响最终的设计选择以及招新效果和社团形象。在正式发言前，你已经对该问题形成了一个初步看法。

请选择，并点击按钮。
""")
    
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
