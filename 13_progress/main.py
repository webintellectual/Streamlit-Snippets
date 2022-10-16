import streamlit as st

import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

st.info("Information")
st.balloons()