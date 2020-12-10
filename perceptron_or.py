def perceptron_or(a0,a1,a2,b0,b1,b2):
  while True:
    net = a0 * b0 + a1 * b1 + a2 * b2
    print('net: ', net)

    if net > 0: 
      y = 1
    else: 
      y = 0
    print('Saida: ', y)

    if a1 == 0 and a2 == 0:  #entradas 0 e 0 - saída 0
      v = 0
    if a1 == 0 and a2 == 1:  #entradas 0 e 1 - saída 1
      v = 1 
    if a1 == 1 and a2 == 0:  #entradas 1 e 0 - saída 1
      v = 1 
    if a1 == 1 and a2 == 1:  #entradas 1 e 1 - saída 1
      v = 1
    print('Saida esperada: ', v)

    if y == v: #se y (saida) = t (esperado)
      print('Finalizado!')
      print('bias: ', a0)
      print('x0: ', a1)
      print('x1: ', a2)
      print('w0: ', b0)
      print('w1: ', b1)
      print('w2: ', b2)
      print('\n')
      break

    else: 
      print('Redefinir pesos')
      n = 0.1
      b0 = b0 + n*(v - y) * a0
      b1 = b1 + n*(v - y) * a1
      b2 = b2 + n*(v - y) * a2
      print('bias: ', a0)
      print('x0: ', a1)
      print('x1: ', a2)
      print('w0: ', b0)
      print('w1: ', b1)
      print('w2: ', b2)
      print('\n')


a0 = -1 #bias
a1 =  0 #x0 
a2 =  1 #x1

#pesos
b0 =  0.7 #peso do bias
b1 = -0.3 #w0
b2 =  0.4 #w1

perceptron_or(a0,a1,a2,b0,b1,b2)
