# 📦 Automação de Inventário de Equipamentos de TI

Este projeto em Python realiza a automação de um inventário de equipamentos de TI a partir de um arquivo CSV, identificando:

- Equipamentos sem responsável definido  
- Equipamentos com garantia vencida  

Ao final, o sistema gera um relatório no terminal com as informações filtradas.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Biblioteca csv
- Módulo datetime
- Ambiente virtual (venv)

---

## 📁 Estrutura do projeto

automacao-inventario/ │ ├── inventario.csv ├── inventario.py ├── funcoes.py └── README.md

---

## 📌 Funcionalidades

✔ Leitura automática de dados do CSV  
✔ Conversão de registros em dicionários Python  
✔ Validação de campos vazios (responsável)  
✔ Cálculo de garantia com base na data de compra  
✔ Geração de relatório organizado  

---

## 📊 Exemplo de regras aplicadas

- Equipamentos sem usuário cadastrado são sinalizados  
- Garantia é calculada somando meses convertidos em dias  
- Itens com data inferior à data atual são marcados como vencidos  

---

## ▶ Como executar o projeto

1. Clone o repositório:

bash

git clone https://github.com/Igor97-dev/automacao-inventario

2. Acesse a pasta:

cd automacao-inventario

3. Execute:
python inventario.py

## 📈 Objetivo do projeto

Projeto criado para praticar automação de tarefas comuns na área de Suporte de TI e iniciar o desenvolvimento de soluções voltadas para gestão de ativos, inventário e controle de equipamentos.

## 👨‍💻 Autor

Igor Nascimento

Analista de Suporte de TI