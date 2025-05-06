import streamlit as st
import random

st.set_page_config(page_title="Cartão de Aniversário", page_icon="🎉🎈")
st.title("Feliz Aniversário!🎉🎈")
st.image("https://tenor.com/rf42IVHSMqU.gif")

frases=[
    "Você tá velha, mas tá top!", 
    "Continue fingindo maturidade, tá dando certo!",
    "Mais um ano de caos com estilo!",
    "Viva mais, pire menos!", 
]

if st.button("Me dê uma frase especial"):
    st.write(random.choice(frases))
