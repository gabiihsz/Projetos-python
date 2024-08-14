velocidade = float(input('Qual sua velocidade?'))
if velocidade <=80:
    print('ok, sem problemas')
elif velocidade >80:
      print('você será multado!!!')
      qtdemulta = velocidade - 80.0
      valormulta = 7.0 * qtdemulta
      print('você pagará R${:.2f{'.format(valormulta))
print('fim do programa')