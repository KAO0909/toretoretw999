import streamlit as st
import pandas as pd
import openai
import os

# 設定 OpenAI API 金鑰（建議改為環境變數）
openai.api_key = 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

# 設定網頁標題
st.set_page_config(page_title="日文詞彙查詢工具", layout="centered")
st.title("📖 日文詞彙查詢工具（雲端同步 + AI 補翻譯）")

# 從 Google Sheets 載入資料
sheet_url = "https://docs.google.com/spreadsheets/d/1KNmZnyS63zxPtYqXU5cfQlUuvbDam63t/export?format=csv"
df = pd.read_csv(sheet_url)

# 顯示搜尋欄
query = st.text_input("🔍 請輸入日文詞彙或句子：")

# 執行查詢
if query:
    matches = df[df['日文原文'].str.contains(query, na=False, case=False)]
    if not matches.empty:
        st.success(f"找到 {len(matches)} 筆結果：")
        st.dataframe(matches)
    else:
        st.warning("詞表中找不到，正在使用 GPT 補翻譯...")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一個專業的日文翻譯，請將輸入的日文翻譯為繁體中文。"},
                    {"role": "user", "content": query}
                ]
            )
            translated = response.choices[0].message.content.strip()
            st.markdown(f"💡 GPT 翻譯結果：**{translated}**")
        except Exception as e:
            st.error("❌ GPT 翻譯失敗，請檢查 API 設定或稍後再試。")
else:
    st.info("請輸入日文詞彙或句子開始查詢。")
