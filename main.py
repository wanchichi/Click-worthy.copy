import streamlit as st

from utils import generate_xiaohongshu


st.header("爆款文案AI🤖写作助手 ✏️")
with st.sidebar:
    openai_api_key = st.text_input("需要先输入OpenAI API密钥嗷：", type="password")
    st.markdown("[点击这里OpenAI API密钥~](https://platform.openai.com/account/api-keys)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API密钥")
    st.stop()
if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### 标题1")
        st.write(result.titles[0])
        st.markdown("##### 标题2")
        st.write(result.titles[1])
        st.markdown("##### 标题3")
        st.write(result.titles[2])
        st.markdown("##### 标题4")
        st.write(result.titles[3])
        st.markdown("##### 标题5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### 正文")
        st.write(result.content)
