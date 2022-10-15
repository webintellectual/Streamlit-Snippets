import streamlit as st

import time
@st.cache
def ret_time(a):
    time.sleep(4)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time("1")) # will take 4 sec to run and then store result to chache
if st.checkbox("2"):
    st.write(ret_time("1")) # this will not take 4 sec to run, directly fetch result from cache
if st.checkbox("3"):
    st.write(ret_time("2")) # this is a different combination, so again run from scratch