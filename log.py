import streamlit as st
import logging

logger = logging.getLogger("simple_logger")

st.title("测试日志")

if st.button("点击开始记录日志"):
    print("01 - This is a print info - B01")
    logger.info("02 - Still running task .")
    logger.info("03 - Still running task ... ")
