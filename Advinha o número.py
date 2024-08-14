import random
 x = int(random.randint(0,5))
 n = int(input('tente advinhar qual numero foi sorteado: '))
 if n==x:
     print('você acertou !!!!!!')
 else:
     print('você errou')
print('numero = {}'.format(x))