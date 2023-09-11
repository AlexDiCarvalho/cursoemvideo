preco =float(input('Qual o preço do produto?: R$'))
desc = preco - (preco * 5/100)
print('O preço do produto com o desconto de 5%, fica:{:.2f} R$'.format(desc))