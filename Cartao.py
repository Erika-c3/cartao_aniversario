import streamlit as st
import random

st.set_page_config(page_title="Lariê oh oh oh", page_icon="🎉🎈")
st.title("Feliz Aniversário!🎉🎈")
st.image("https://i.pinimg.com/474x/22/a5/5d/22a55d321d95a454dc75e872af4640ca.jpg")

frases=[
    "Você tá velha, mas tá top!", 
    "Continue fingindo maturidade, tá dando certo!",
    "Mais um ano de caos com estilo!",
    "Viva mais, pire menos!", 
]

if st.button("Me dê uma frase especial"):
    st.write(random.choice(frases))
