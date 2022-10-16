import streamlit as st

st.title("Registration Form")

first, last = st.columns(2) # returns two containers
first.text_input("First Name") # we can add anything to these container objects
last.text_input("Last Name")

email,mob = st.columns([3,1]) # divide the col into 3:1 ratio b/w these 2 containers
# email container will be 3 times bigger than mob container

email.text_input("Email ID")
mob.text_input("Mob Number")

user,pw,pw2 = st.columns(3)
user.text_input("User Name")
pw.text_input("Enter Password", type="password")
pw2.text_input("Retype Password", type="password")

ch,bl,sub = st.columns(3)
ch.checkbox("I Agree")
sub.button("Submit")