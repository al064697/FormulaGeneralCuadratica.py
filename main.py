import math

# Declarando variables
A = int(input("Introduce un valor para A: "))
B = int(input("Introduce un valor para B: "))
C = int(input("Introduce un valor para C: "))

if (A == 0) & (B == 0):
    print('La ecuacion es denegada')
elif (A == 0) & (B != 0):
    print(f'existe una raiz unica con valor de {C / B}')
else:
    # Calculando discriminante
    discriminante = (B ** 2) - (4 * A * C)

    # Sacando raices cuadradas
    if (discriminante >= 0):
        print('Existen dos raices cuadradas: ')
        print(f'X1 = {-B + (math.sqrt(discriminante)) / (2 * A)}')
        print(f'X2 = {-B - (math.sqrt(discriminante)) / (2 * A)}')
    elif discriminante == 0:
        print('existe una raiz unica real:')
        print(f'X1 = {-B + (math.sqrt(discriminante)) / (2 * A)}')
        print(f'X2 = {-B - (math.sqrt(discriminante)) / (2 * A)}')

        # Sacando raices cuadradas compuestas
    elif discriminante < 0:
        print('Existen dos raices compuestas')
        print(f'X1 = {(- B / 2 * A)} + {(math.sqrt(abs(discriminante))) / (2 * A)} i')
        print(f'X2 = {(- B / 2 * A)} - {(math.sqrt(abs(discriminante))) / (2 * A)} i')