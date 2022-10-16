import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("ggplot")
data={ # dictionary
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
df = pd.DataFrame(data=data)

# Main code starts from here:-
rad=st.sidebar.radio("Navigation",['Home','About us'])

if rad=='About us':
    st.write("This web app is developed by Akshay Rajput for demonstration of streamlit")
if rad=='Home':
    col2=st.sidebar.multiselect("Select a column", df.columns) # list of name of cols of df is passed
    fig, ax = plt.subplots()
    ax.plot(df['num'], df[col2])
    st.pyplot(fig)
