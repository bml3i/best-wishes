import streamlit as st

from utils import create_text_image

# CSS Styles
st.markdown("""
<style>
h1 {
    font-size: 30px !important;
}
            
img {
    width: 50% !important;  /* 设置图像宽度为父容器的50% */
}
</style>
""", unsafe_allow_html=True)

st.title("🌸 美好祝愿 - 随心生成 🌸")

your_name = st.text_input("你的名字?")
st.write("your name: " + your_name)

initial_text = """明日朝阳映瑞雪，
磊落人生喜气多。
祝愿声声传四海，
您心所愿皆成真。
新春佳节福星照，
春风送暖入屠苏。
快意人生添欢笑，
乐享天伦共此时。"""

best_wishes = st.text_area("输入一段话吧?", value=initial_text, height=210)

st.write(best_wishes)

# 创建一个按钮
if st.button("生成图片"):
    # 当按钮被点击时，生成图片
    image = create_text_image(my_text = best_wishes, delimiters=r'[\n]')
    # 显示生成的图片
    st.image(image)

