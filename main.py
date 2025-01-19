import streamlit as st

from utils import create_text_image

st.title("Best Wishes 🌸")

initial_text = """明日朝阳映瑞雪，
磊落人生喜气多。
祝愿声声传四海，
您心所愿皆成真。
新春佳节福星照，
春风送暖入屠苏。
快意人生添欢笑，
乐享天伦共此时。"""

para = st.text_area("输入一段话吧?", value=initial_text )

st.write(para)

# 创建一个按钮
if st.button("生成图片"):
    # 当按钮被点击时，生成图片
    image = create_text_image(my_text = para)
    # 显示生成的图片
    st.image(image, caption="生成的图片")

