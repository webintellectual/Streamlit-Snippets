import streamlit as st
st.error("Error box")
st.success("Success box")
st.info("Information")
st.exception(RuntimeError("this is an exception")) # takes valid exception as argument
st.warning("This is a warning")