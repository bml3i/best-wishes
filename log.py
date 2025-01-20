import streamlit as st
import logging
import requests

def get_remote_ip() -> str:
    if "my_ip" not in st.session_state:
        data = requests.get("https://api-bdc.net/data/client-ip").json()
        st.session_state["my_ip"] = data["ipString"]
        return st.session_state["my_ip"]
    else:
        return st.session_state["my_ip"]

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user_ip = get_remote_ip()
        return super().filter(record)

logger = logging.getLogger(st.__name__)
if not logger.handlers:
    logger.propagate = False
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(user_ip)s] - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.addFilter(ContextFilter())
    handler.setFormatter(formatter)
    logger.addHandler(handler)

st.title("Logger Testing")

logger.info("Inside main")

text = st.sidebar.text_input("Text:")
logger.info(f"This is the text: {text}")

data = requests.get("https://api-bdc.net/data/client-ip").json()
st.write(data["ipString"])