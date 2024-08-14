ano = int(input('Informe o ano que deseja saber se é ou não bissexto:'))
if ano%4 ==0:
    if ano % 400 ==0:
        print('não é bissexto')
    else:
         print('é bissexto')

else:
    print('não é bissexto')
print('fim do programa')