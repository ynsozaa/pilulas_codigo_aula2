import math
#entradas
assinantes = int(input ('Assinantes Atuais: '))
mensalidade = float(input('Valor da Mensalidade: '))
taxa = float (input('Taxa de Crescimento Mensal (%): '))/100
meses = int(input('Meses de Projeção: '))
#processamento
assinantes_finais = assinantes * math.pow((1+taxa), meses)
receita_final = assinantes_finais * mensalidade
#saida
print(f'Assinantes Estimados: {assinantes_finais:.0f}')
print(f'Receita Mensal Estimada R$:{receita_final:.2f}')
