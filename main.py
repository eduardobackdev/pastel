import streamlit as st
import pandas as pd
import numpy as np
import urllib.parse

st.write("""
         # Faça seu pedido para Eduardo
          Faça seu pedido abaixo:""")   

opcoes = ["Pastel", "Coxinha", "Esfiha"]
data_entrega = st.date_input("Escolha a data de entrega:")

pedido = st.selectbox("Escolha o salgado: ", opcoes)

if pedido == "Pastel":
    st.selectbox("Escolha o recheio do pastel:", ["Carne", "Banana e Queijo", "Frango com Catupiry"])
elif pedido == "Coxinha":
    st.selectbox("Escolha a massa:", ["Macaxeira", "Trigo"])
    st.selectbox("Escolha o recheio da coxinha:", ["Frango", "Carne"])
elif pedido == "Esfiha":    
    st.selectbox("Escolha o recheio da esfiha:", ["Carne", "Mista", "Calabresa"])

if st.button("Fazer pedido"):
    telefone = "5592984374299"

    mensagem = f"Novo pedido:\n\n Salgado: {pedido}\n"
    mensagem_codificada = urllib.parse.quote(mensagem)

    link = f"https://wa.me/{telefone}?text={mensagem_codificada}"

    st.success("Pedido pronto! Clique abaixo para enviar no WhatsApp ")
    st.markdown(f"[Enviar pedido]({link})", unsafe_allow_html=True)



st.write(""" 
         
         # Valor: R$ 5,00 cada
            """)


