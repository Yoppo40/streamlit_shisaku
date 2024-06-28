import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API認証
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\doyou\\root\\shisaku-427507-f81764e9a169.json', scope)
client = gspread.authorize(creds)

# スプレッドシートのデータを取得
spreadsheet = client.open("Shisaku")
worksheet = spreadsheet.sheet1  # 1つ目のシートを使用
data = worksheet.get_all_records()

# データフレームに変換
df = pd.DataFrame(data)

# Streamlitアプリケーションの設定
st.title("Google Sheets Data Visualization")
st.write("以下はGoogle Sheetsから取得したデータです。")

# データ表示
st.dataframe(df)

# グラフの作成
st.write("データをグラフ化します。")
st.line_chart(df)

# グラフのオプション
chart_type = st.selectbox("グラフの種類を選択してください。", ["line", "bar", "area"])
if chart_type == "line":
    st.line_chart(df)
elif chart_type == "bar":
    st.bar_chart(df)
else:
    st.area_chart(df)
