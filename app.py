import streamlit as st
st.write("""
# Substraction of two Numbers
""")
st.header('User Input parameters')


first_number=st.number_input("First Number")
    
second_number=st.number_input("Second Number")
answer=first_number-second_number
st.subheader('Result')
st.write(answer)