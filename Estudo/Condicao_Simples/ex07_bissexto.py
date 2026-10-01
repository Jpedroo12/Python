from datetime import date
ano = int(input('Digite um ano, digite 0 para ver o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} NÃO É BISSEXTO'.format(ano))



#Código antigo
'''if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('É BISSEXTO')
        else:
            print('NÃO É BISSEXTO')
    else:
        print('É BISSEXTO')
else:
    print('NÃO É BISSEXTO')'''
