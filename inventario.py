import csv
from datetime import datetime, timedelta
from funcoes import escreva



# Transformando o arquivo csv em uma lista de dicionários

equipamentos = []

with open('inventario.csv', newline= '', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        equipamentos.append(linha)

# Verificando equipamnetos sem responsável

equipamentos_sem_responsavel = []

for eq in equipamentos:
    if eq['usuario'].strip() == '':
        equipamentos_sem_responsavel.append(eq)

print(equipamentos)
print(equipamentos_sem_responsavel)

# verificando equipamentos com garantia vencida

garantia_vencida = []

hoje = datetime.today()

for eq in equipamentos:
    data_da_compra = datetime.strptime(eq['data_compra'], '%Y-%m-%d')
    meses_da_garantia = int(eq['garantia_meses'])
    fim_da_garantia = data_da_compra + timedelta(days=meses_da_garantia * 30)


    if fim_da_garantia < hoje:
        garantia_vencida.append(eq)


# Gerando relatório

escreva('Relatório de inventário', pont=True)

print('Equipamentos sem responsável: ')
for eq in equipamentos_sem_responsavel:
    print(f' - {eq["patrimonio"]} ({eq["tipo"]})')

print('Equipamentos com garantia vencida: ')
for eq in garantia_vencida:
    print(f' - {eq["patrimonio"]} ({eq["tipo"]})')










