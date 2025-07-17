import streamlit as st
import pandas as pd

st.title('BRICS Literacy Dashboard')
df = pd.read_csv('../../data/brics.csv')
st.dataframe(df)