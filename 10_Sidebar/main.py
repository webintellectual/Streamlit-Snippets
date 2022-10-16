import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
data={ # dictionary
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
df = pd.DataFrame(data=data) # converting dictionary to dataframe

# main code starts from here:-
# st.sidebar.selectbox("select a number", [1,2,3,4,5])
col=st.sidebar.selectbox("Select a column", df.columns) # list of name of cols of df is passed
fig, ax = plt.subplots()
ax.plot(df['num'], df[col])
st.pyplot(fig)

col2=st.sidebar.multiselect("Select a column", df.columns) # list of name of cols of df is passed
fig, ax = plt.subplots()
ax.plot(df['num'], df[col2])
st.pyplot(fig)