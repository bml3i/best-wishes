import streamlit as st
import os
import time
from datetime import datetime
import pytz

from st_copy_to_clipboard import st_copy_to_clipboard
from utils import create_text_image, count_any_chars, generate_my_blessing

# CSS Styles
st.markdown("""
<style>
h1 {
    font-size: 24px !important;
}
            
img {
    width: 50% !important; 
}

</style>
""", unsafe_allow_html=True)

# Set the timezone to Shanghai
shanghai_tz = pytz.timezone('Asia/Shanghai')

# Get the current date
current_date = datetime.now(shanghai_tz).date()

# Display the current date and time in Shanghai
# st.write(f"Current date and time in Shanghai: {current_date}")

if "chance_number" not in st.session_state:
    st.session_state.chance_number = 3


st.title(f"🌸 美好祝愿 - 随心生成 🌸")


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

if 'last_click_time' not in st.session_state:
    st.session_state.last_click_time = 0

with column11:
    your_name = st.text_input("你的名字/对方的名字?")
    if(len(your_name) > 0 and count_any_chars(your_name) != 2): 
        your_name_alert = st.info("请输入2个汉字")

with column12: 
    selected_wish_type = st.selectbox("祝福短语模板", options=["------ 用你的名字送去祝福 ------","XX祝您新春快乐", "XX祝您全家幸福",
        "------ 用对方的名字送去祝福 ------", "XX蛇年吉祥如意", "XX春节笑口常开", "XX蛇年健康长寿"])

column21, column22 = st.columns(2)

with column21:
    if selected_wish_type and your_name and your_name_alert is None and "XX" in selected_wish_type: 
        one_sentence_blessing_val = selected_wish_type.replace("XX", your_name)
        one_sentence_blessing = st.text_input("default", value=one_sentence_blessing_val, label_visibility="hidden")
    else:
        one_sentence_blessing = st.text_input("default", value="", label_visibility="hidden")


with column22:
    st.text("")
    if st.button("随心生成") and one_sentence_blessing: 
        print("one_sentence_blessing: " + one_sentence_blessing)
        current_time = time.time()
        if current_time - st.session_state.last_click_time >= 10:
            st.session_state.last_click_time = current_time

            if st.session_state.chance_number <= 0: 
                st.error("使用次数已达到上限，关注微信号解锁更多使用次数。")
            else: 
                with st.spinner("AI正在创作中,请稍后..."):
                    result = generate_my_blessing(theme=one_sentence_blessing, openai_api_key=st.secrets["openai_api_key"])
                    st.session_state["my_blessing"] = result.content
                    st.session_state.chance_number = st.session_state.chance_number - 1
        else:
            st.warning("操作频繁，请稍后再试。")


best_wishes = st.text_area("default", value=st.session_state["my_blessing"], height=220, label_visibility="hidden")

if st.button("生成图片 & 复制祝福"):
    image = create_text_image(my_text = best_wishes, delimiters=r'[\n]')
    st_copy_to_clipboard(best_wishes)
    st.image(image)

footer = st.container()
with footer:
    st.write("关注微信公众号\"小众生活评测\"，回复内容“美好祝愿”，解锁更多权限。")
    st.write(f"(今日剩余次数: {st.session_state.chance_number})")

print(os.environ.get('HTTP_PROXY'))
print(os.environ.get('HTTPS_PROXY'))
