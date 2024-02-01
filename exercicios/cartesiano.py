
coordenada_de_x = float(input('Digite a coordenada de X:'))
coordenada_de_y = float(input('Digite a coordenada de Y:'))

if coordenada_de_y > 0 and coordenada_de_x > 0:
    print('Primeiro Quadrante!')
elif coordenada_de_x < 0 and coordenada_de_y > 0:
    print('Segundo Quadrante!')
elif coordenada_de_x < 0 and coordenada_de_y < 0:
    print('Terceiro Quadrante!')
else:
    print('Quarto Quadrante!')