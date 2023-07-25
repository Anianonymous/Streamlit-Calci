import streamlit as st
from math import *
st.title("Calculator App") 
# [theme]
base="dark"

st.write("---")
 
# input 1
n1=st.number_input(label="enter your first number: ")
#input 2
n2=st.number_input(label="enter your second number: ")

st.write("operation")
opt=st.radio("select your required operation:",("Addition","Subtraction","Multiplication","Division","Power"))
ans=0
def cal():
    if opt=="Addition":
        ans=n1+n2
    elif opt=="Subtraction":
        ans=n1-n2
    elif opt=="Multiplication":
        ans=n1*n2
    elif n2!=0 and opt=="Division":
        ans=n1/n2
    elif opt=="Power":
        ans=n1**n2
    else:ans="undefined"
    st.success(f"result is : {ans}")
    #clicking the button answer is displayed
if st.button("result"):
  #call the function
    cal()
 
