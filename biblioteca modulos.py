import math
num = int (input('digite um número:'))
raizquadrada = math.sqrt(num)
print('Raiz de {} é = {}'.format(num,raizquadrada))
print('Raiz de {} arredondada para próximo inteiro é {}'.format(num,math.ceil(raizquadrada)))
