fatorial = 1
contador = 4.65

while contador > 1:
    # print(f'{contador:,.2f} x ', end='')  # end = '' , alinhou as coisas, sem ele seria na vertical
    print('{%g} x '%contador, end='')
    fatorial *= contador
    contador -= 1
print("1 = ",round(fatorial,2))
