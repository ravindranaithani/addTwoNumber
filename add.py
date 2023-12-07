import streamlit as st
st.title('Multiply Two Number')
first_number = st.number_input('Enter the first number')
second_number = st.number_input('Enter the second number')
def multiply(first_number, second_number):
    result = first_number * second_number
    return result
st.write(" This is the result:" ,multiply(first, second))
  
