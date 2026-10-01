velocidade = float(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7.0
    print(f"MULTADO! Excedeu o limite de 80 km/h. O valor da multa é R$ {multa:.2f}")
else:
    print('Tudo norma! -_-')