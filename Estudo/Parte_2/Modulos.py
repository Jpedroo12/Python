'''Importação de toda a blioteca'''
import math
import random
'''PIP install/uninstall, é o comando que instala modulos externos'''
'''Gera um numero inteiro de 1 a 100'''
n = random.randint(1,100)
'''função de raiz quadrada'''
raiz  =  math.sqrt(n) 
'''math.ceil(arredonda para cima)'''
print('a raiz de  {} é igual a {}'.format(n, math.ceil(raiz)))

