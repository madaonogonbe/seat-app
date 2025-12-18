# 🌐 URL共有できるWeb版 席替えアプリ（Streamlit）
# ※ Google Colabでは「コード作成のみ」
# ※ 実際の公開は Streamlit Community Cloud を使います

# ===============================
# ファイル名: app.py
# ===============================

import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="席替えアプリ", layout="centered")

st.title("🪑 席替えアプリ")
st.caption("URL共有OK・スマホ対応")

# ---- 入力 ----
st.subheader("👥 名簿")
name_text = st.text_area(
    "1行に1人ずつ名前を入力",
    "佐藤\n鈴木\n高橋\n田中\n伊藤\n渡辺\n山本\n中村\n小林\n加藤\n吉田\n山田"
)

students = [n for n in name_text.split("\n") if n.strip()]

st.subheader("🪑 席の形")
rows = st.number_input("行", min_value=1, max_value=10, value=3)
cols = st.number_input("列", min_value=1, max_value=10, value=4)

# ---- 席替え ----
if st.button("🔁 席替えする"):
    names = students.copy()
    random.shuffle(names)

    while len(names) < rows * cols:
        names.append("空席")

    table = []
    for i in range(rows):
        table.append(names[i*cols:(i+1)*cols])

    df = pd.DataFrame(table)

    st.subheader("📋 席替え結果")
    st.dataframe(df, use_container_width=True)

    # CSV保存
    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="💾 CSVをダウンロード",
        data=csv,
        file_name="seats.csv",
        mime="text/csv"
    )

st.markdown("---")
st.caption("学校・クラス・イベントで自由に使えます")
