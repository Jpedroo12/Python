DistanciaKm = float(input('Qual a distância da sua viagem em km?\n'))

if DistanciaKm <= 200:
    passagem = DistanciaKm * 0.5
    print('você vai ser cobrado pela passagem:{:.2f}'.format(passagem))
else:
    passagem = DistanciaKm * 0.45
    print('você vai ser cobrado pela passagem: {:.2f}'.format(passagem))
