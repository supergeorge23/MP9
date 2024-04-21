import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

st.title('My First Streamlit App')
st.header('This is a header')
st.write('distilgpt2 model trial: You can write anything!')
# Load a text generation model
generator = pipeline('text-generation', model='distilgpt2')
user_input = st.text_input("Enter your text:")
if user_input:
    with st.spinner('Generating...'):
        responses = generator(user_input, max_length=50)
        st.text(responses[0]['generated_text'])



number = st.slider('Select a number:', 0, 100, 50)  # min, max, default
st.write('You selected:', number)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Hello, column 1!")

with col2:
    st.header("Column 2")
    st.write("Hello, column 2!")

st.markdown('**Bold Text:** Here is some bold text!')



fig, ax = plt.subplots()
ax.hist([10, 20, 30, 40, 50], bins=[0, 10, 20, 30, 40, 50])
st.pyplot(fig)





