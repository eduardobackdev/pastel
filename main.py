import streamlit as st
import pandas as pd
import urllib.parse
from datetime import date

#defini classes, 

class Pedido:
    def __init__(self, tipo, recheio, massa, data_entrega, quantidade):
        self.tipo = tipo
        self.recheio = recheio
        self.massa = massa
        self.data_entrega = data_entrega
        self.quantidade = quantidade

    def gerar_mensagem(self):
        return (
            f"Novo pedido:\n"
            f"Tipo: {self.tipo}\n"
            f"Recheio: {self.recheio}\n"
            f"Massa: {self.massa if self.massa else 'Nenhuma'}\n"
            f"Data: {self.data_entrega}\n"
            f"Quantidade: {self.quantidade}"
        )

    def gerar_link_whatsapp(self, telefone):
        mensagem = self.gerar_mensagem()
        mensagem_codificada = urllib.parse.quote(mensagem)
        return f"https://wa.me/{telefone}?text={mensagem_codificada}"


class Cardapio:
    def __init__(self):
        self.opcoes = ["Pastel", "Coxinha", "Esfiha"]
        self.recheios = {
            "Pastel": ["Carne", "Banana e Queijo", "Frango com Catupiry"],
            "Coxinha": ["Frango", "Carne"],
            "Esfiha": ["Carne", "Mista", "Calabresa"]
        }
        self.massas = ["Macaxeira", "Trigo"]

    def get_recheios(self, tipo):
        return self.recheios.get(tipo, [])


# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(
    page_title="Salgados do Eduardo",
    page_icon="🚩",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Faça seu pedido para Eduardo")

cardapio = Cardapio()

# ESCOLHAS DO USUÁRIO

data_entrega = st.date_input("Escolha a data de entrega:", min_value=date.today())
tipo = st.selectbox("Escolha o salgado:", cardapio.opcoes)

recheio = st.selectbox("Escolha o recheio:", cardapio.get_recheios(tipo))

massa = None
if tipo == "Coxinha":
    massa = st.selectbox("Escolha a massa:", cardapio.massas)

quantidade = st.number_input("Quantidade:", min_value=1, max_value=100, value=1)

# BOTÃO DE PEDIDO

if st.button("Fazer pedido"):
    pedido = Pedido(tipo, recheio, massa, data_entrega, quantidade)
    telefone = "5592984374299"

    link = pedido.gerar_link_whatsapp(telefone)

    st.success("Pedido pronto! Clique abaixo para enviar no WhatsApp:")
    st.markdown(f"[ Enviar pedido]({link})")


# RODAPÉ
st.markdown("## Valor: R$ 5,00 cada")