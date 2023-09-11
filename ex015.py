dias = int(input('Quantos dias pretende alugar o carro?'))
km = float(input('Quantos km pretende utilizar com o carro?'))
pago = ( dias * 60) + (km * 0.15)
print('O valor do aluguel será de: {} R$'.format(pago))
