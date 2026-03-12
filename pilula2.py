import random
#entradas
cotacao = float(input('Cotação Atual do Dolar: '))
#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print(f'Variação Simulada: {variacao:.3%}')
print(f'Nova Cotação: R$ {nova_cotacao:.4f}')
