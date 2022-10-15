from email.policy import default
import streamlit as st
st.title("WIDGETS")

st.button("Press me!")
if st.button("Press me too!"): # returns boolean value, true if button is pressed
    st.write("Waah! kya dabaya h!")

name = st.text_input("Input text:")
st.write(name)

address = st.text_area("Input address:")
st.write(address)

st.date_input("Enter date:")

st.time_input("Enter time:")

if st.checkbox("Accept T&C", value=False): # param2 is defalut state. True => checked by defualt
    st.write("Thank you :)")

v1=st.radio("Colours", ['r','g','b'],index=0) # param3 is option which will be selected by default

v2=st.selectbox("Colours", ['r','g','b'],index=0)
st.write(v1,v2)

v3=st.multiselect("Colours", ['r','g','b'])
st.write(v3)

st.slider("Variable slider", min_value=10, max_value=100, value=95)

st.number_input("Variable slider", min_value=10, max_value=100, value=92, step=2)

img=st.file_uploader("Upload an image:")
st.image(img)