import streamlit as st
import pandas as pd

csv_file='https://docs.google.com/spreadsheets/d/e/2PACX-1vSxN7ZYdU8BJ5GJ9MDFoUIeEcHgNLOZhVdMQaMUs0nKP_zgyGb6NAAYjJEofROV86O5kRwszJOEqI7U/pub?gid=0&single=true&output=csv'
df=pd.read_csv(csv_file)
st.data_editor(
    df,
    column_config={
        "apps": st.column_config.TextColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        ),
                "url": st.column_config.ImageColumn(
            "Preview Image", help="Streamlit app preview screenshots"
        )
    },
    width=1000,
    height=1000,
    hide_index=True,
)