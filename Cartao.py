import streamlit as st
import random

st.set_page_config(page_title="Lariê oh oh oh", page_icon="🎉🎈")
st.title("Feliz Aniversário!🎉🎈")
st.image("https://i.pinimg.com/474x/22/a5/5d/22a55d321d95a454dc75e872af4640ca.jpg")

frases=[
    "Você tá velha, mas tá top! (um abraço)", 
    "Continue fingindo maturidade, tá dando certo! (um abraço)",
    "Viva mais, pire menos! (um abraço)", 
]

if st.button("Click aqui para abrir seu presente!🎁"):
    st.write(random.choice(frases))
    st.image("https://i.pinimg.com/736x/fb/59/15/fb5915b35c5698740f54916f15537f39.jpg")
