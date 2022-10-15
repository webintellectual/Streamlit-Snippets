import streamlit as st
import pandas as pd
import numpy as np

# preparing data
a = [1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape(2,4)
dic = {
    "name":["Akshay Rajput"], #only use list as value for st.dataframe
    "city":["Bhiwani"]
}
data = pd.read_csv("05_Display_data/dataset.csv")

# st.dataframe
st.header("st.dataframe")
st.text("list:")
st.dataframe(a)
st.text("numpy array:")
st.dataframe(nd)
st.text("dictionary:")
st.dataframe(dic)
st.text("adjusting width of dataframe:")
st.dataframe(data,width=500,height=500)

# st.table
st.header("st.table")
st.table(data)
st.table(dic)