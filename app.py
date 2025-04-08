import streamlit as st
import pandas as pd

# 設定網頁標題
st.set_page_config(page_title="日文詞彙查詢工具", layout="centered")
st.title("📖 日文詞彙查詢工具（雲端同步版）")

# 從 Google Sheets 載入資料
sheet_url = "https://docs.google.com/spreadsheets/d/1KNmZnyS63zxPtYqXU5cfQlUuvbDam63t/export?format=csv"
df = pd.read_csv(sheet_url)

# 顯示搜尋欄
query = st.text_input("🔍 請輸入日文詞彙：")

# 執行查詢
if query:
    matches = df[df['日文原文'].str.contains(query, na=False, case=False)]
    if not matches.empty:
        st.success(f"找到 {len(matches)} 筆結果：")
        st.dataframe(matches)
    else:
        st.warning("找不到對應詞彙，請確認輸入是否正確。")
else:
    st.info("請輸入日文詞彙開始查詢。")
