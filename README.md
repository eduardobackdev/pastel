# Sistema de Pedidos - Eduardo Salgados 

Este é um aplicativo web interativo desenvolvido em **Python** com o framework **Streamlit**. O objetivo da ferramenta é automatizar e organizar o processo de pedidos de salgados para o Eduardo, integrando a interface de escolha diretamente com o WhatsApp.

##  Funcionalidades

* **Menu Dinâmico:** As opções de recheio e massa ajustam-se automaticamente conforme o salgado selecionado (Pastel, Coxinha ou Esfiha).
* **Agendamento de Entrega:** Inclui um seletor de data para facilitar a organização da produção.
* **Integração com WhatsApp:** Gera um link automático com a mensagem do pedido já preenchida para envio rápido via `wa.me`.
* **Transparência de Preços:** Exibição clara do valor unitário de cada item no rodapé da página.

## Tecnologias Utilizadas

* **Python:** Linguagem base do projeto.
* **Streamlit:** Framework utilizado para a interface de utilizador.
* **Urllib.parse:** Biblioteca para codificação de caracteres na URL do WhatsApp.
## Como rodar o projeto
Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Você precisará instalar o Streamlit:

````bash
pip install streamlit
````
### Execução
- Salve o arquivo main.py em uma pasta.

- Abra o terminal ou prompt de comando nessa pasta.

Execute o comando:

````Bash
streamlit run main.py
````
## Estrutura do Código

O arquivo `main.py` contém toda a lógica da aplicação, incluindo:
1. **Configuração da Interface:** Títulos e textos explicativos.
2. **Campos de Entrada:** Captura da data, tipo de salgado e especificações (recheio/massa).
3. **Lógica de Envio:** Tratamento da mensagem e criação do link dinâmico para o contacto `+55 92 98437-4299`.



