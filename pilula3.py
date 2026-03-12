import datetime
#entrada
data_compra = input('Digite a Data da Compra d/m/aaaa: ')
meses = int(input('Prazo de Garantia: '))
#processamento
data_inicial = datetime.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + datetime.timedelta(days=meses * 30)
#saida
print(f'Garantia Valida Ate {data_final.strftime('%d/%m/%Y')}')
print(f'Dia da Semana: {data_final.strftime('%A')}')
