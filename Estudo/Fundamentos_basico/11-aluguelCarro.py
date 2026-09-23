dias = int(input('Quanto dias foram alugados?'))
km = float(input('Quantos km rodados?'))

pago = dias * 60 + (km * 0.15)

print('o total a pagar é de R${:.2f}'.format(pago))