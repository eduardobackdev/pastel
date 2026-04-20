import streamlit as st
import pandas as pd
import numpy as np
import urllib.parse

# Configurações da página
st.set_page_config(
    page_title="Salgados do Eduardo",
    page_icon="🚩",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Título principal
st.write("""
         # Faça seu pedido para Eduardo
          Faça seu pedido abaixo:""")   

# Viariaveis para definir os tipos de salgados, recheios e massas

opcoes = ["Pastel", "Coxinha", "Esfiha"]
recheio_pastel = ["Carne", "Banana e Queijo", "Frango com Catupiry"]
massa = ["Macaxeira", "Trigo"]
recheio_coxinha = ["Frango", "Carne"]
recheio_esfiha = ["Carne", "Mista", "Calabresa"]

# Campo para escolher a data de entrega, tipo de salgado e recheio

data_entrega = st.date_input("Escolha a data de entrega:")
fazer_pedido = st.selectbox("Escolha o salgado: ", opcoes)
recheio_escolhido = recheio_pastel if fazer_pedido == "Pastel" else (recheio_coxinha if fazer_pedido == "Coxinha" else recheio_esfiha)  
quantidade_pedido = st.number_input("Quantidade:", min_value=1, max_value=100, value=1) 

# Exibir opções de recheio com base no tipo de salgado escolhido

if fazer_pedido == "Pastel":
    st.selectbox("Escolha o recheio do pastel:", recheio_pastel) 
elif fazer_pedido == "Coxinha":
    st.selectbox("Escolha a massa:", massa)
    st.selectbox("Escolha o recheio da coxinha:", recheio_coxinha)
elif fazer_pedido == "Esfiha":    
    st.selectbox("Escolha o recheio da esfiha:", recheio_esfiha)


# Variável para armazenar o pedido selecionado
pedido =  fazer_pedido


# Botão para fazer o pedido e gerar o link do WhatsApp
if st.button("Fazer pedido"):
    telefone = "5592984374299"

    mensagem = f" Novo pedido: {pedido}\n Recheio: {recheio_escolhido[0]}\n Massa: {massa[0]}\n Data de entrega: {data_entrega}\n Quantidade: {quantidade_pedido}"            
            
    mensagem_codificada = urllib.parse.quote(mensagem)

    link = f"https://wa.me/{telefone}?text={mensagem_codificada}"

    st.success("Pedido pronto! Clique abaixo para enviar via WhatsApp ")
    st.markdown(f"[Enviar pedido]({link})", unsafe_allow_html=True)



st.write(""" 
         
         # Valor: R$ 5,00 cada
            """)


