import streamlit as st
st.markdown("**Bold** *italic*")
st.markdown("# h1 heading")
st.markdown("> Quote")
st.markdown("---") # horizontal line
st.markdown("[Link](https://github.com/webintellectual)")
st.caption("Hi! I am a caption")

st.latex(r""" Latex: \ \ \ 
\gamma^2+\theta^2=\omega^2""")

j={"json":"1,2,3", "J-son":"4,5,6"}
st.json(j)

cd="""// code

#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
"""
st.code(cd,language="cpp")