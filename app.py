
import streamlit as st
import pandas as pd

# 讀取詞庫 CSV
@st.cache_data
def load_data():
    return pd.read_csv("term_lookup_demo.csv")

df = load_data()

st.title("🎌 詞彙即時查詢工具（日文→繁中）")

query = st.text_input("請輸入日文單詞或句子進行查詢：")

if query:
    matches = df[df['日文'].str.contains(query, na=False)]

    found_terms = []
    for _, row in df.iterrows():
        if row['日文'] in query:
            found_terms.append(row)

    if matches.empty and not found_terms:
        st.warning("找不到對應詞彙，請確認輸入內容是否正確。")

    if not matches.empty:
        st.subheader("🔍 模糊查詢結果")
        st.dataframe(matches)

    if found_terms:
        st.subheader("🧩 整句比對中出現的詞彙")
        st.dataframe(pd.DataFrame(found_terms))
else:
    st.info("請輸入日文詞彙或句子，例如：『ペットボトルカバーは便利です』 或 『スペシャル』")
