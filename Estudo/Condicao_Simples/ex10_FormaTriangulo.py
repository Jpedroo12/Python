r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Testando a condição matemática
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('\033[1;37;45mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m')
#/033[style, text, backgroundm
#\033[0:33:44m
#padrão anci
