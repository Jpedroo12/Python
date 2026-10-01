n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

#Menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

#Maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))

#Código antigo
'''if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print('O maior é: {}\n O menor é: {}'.format(n1, n3))
        else:
            print('O maior é: {}\n O menor é: {}'.format(n1, n2))
if n2 > n1:
    if n2 > n3:
        if n1 > n3:
            print('O maior é: {}\n O menor é: {}'.format(n2, n3))
        else:
            print('O maior é: {}\n O menor é: {}'.format(n2, n1))  

if n3 > n1:
    if n3 > n2:
        if n1 > n2:
            print('O maior é: {}\n O menor é: {}'.format(n3, n2))
        else:
            print('O maior é: {}\n O menor é: {}'.format(n3, n1))  '''
