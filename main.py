import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard

from utils import create_text_image, count_any_chars

# CSS Styles
st.markdown("""
<style>
h1 {
    font-size: 24px !important;
}
            
img {
    width: 50% !important;  /* 设置图像宽度为父容器的50% */
}

</style>
""", unsafe_allow_html=True)

st.title("🌸 美好祝愿 - 随心生成 🌸")

column11, column12 = st.columns(2)

your_name_alert = None

initial_text = """明日朝阳映瑞雪，
磊落人生喜气多。
祝愿声声传四海，
您心所愿皆成真。
新春佳节福星照，
春风送暖入屠苏。
快意人生添欢笑，
乐享天伦共此时。"""

if "my_blessing" not in st.session_state:
    st.session_state["my_blessing"] = initial_text


with column11:
    your_name = st.text_input("你的名字?")
    if(len(your_name) > 0 and count_any_chars(your_name) != 2): 
        your_name_alert = st.info("请输入2个汉字")

with column12: 
    selected_wish_type = st.selectbox("祝福短语模板", options=["XX祝您新春快乐", "XX祝您全家幸福"])


column21, column22 = st.columns(2)

with column21:
    if selected_wish_type and your_name and your_name_alert is None: 
        one_sentence_blessing_val = selected_wish_type.replace("XX", your_name)
        one_sentence_blessing = st.text_input("default", value=one_sentence_blessing_val, label_visibility="hidden")
    else:
        one_sentence_blessing = st.text_input("default", value="", label_visibility="hidden")
    

with column22:
    st.text("")
    if st.button("随心生成"): 
        with st.spinner("AI正在创作中,请稍后..."):
            st.session_state["my_blessing"] = "888"


best_wishes = st.text_area("default", value=st.session_state["my_blessing"], height=210, label_visibility="hidden")


# 创建一个按钮
if st.button("生成图片 & 复制祝福"):
    # 当按钮被点击时，生成图片
    image = create_text_image(my_text = best_wishes, delimiters=r'[\n]')
    st_copy_to_clipboard(best_wishes)
    # 显示生成的图片
    st.image(image)

