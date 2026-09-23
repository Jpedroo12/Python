salario = float(input('Qual é os seu salário?'))
aumento = int(input('Quanto de aumento vai dar em porcentagem?'))
'''Calculo para saber o novo salário com aumento'''
novo = salario + (salario * aumento / 100)

'''apresentação do novo salário'''
print('Um funcionário que ganhava R${:.2f}, com aumento de {}% de aumento, passa a receber R${:.2f}'.format(salario, aumento, novo))