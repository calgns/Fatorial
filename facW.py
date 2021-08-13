fatorial = 1
contador = 4.65

while contador > 1:
    # um jeito de fazer as coisas print(f'{contador:,.2f} x ', end='').
    print('{%g} x ' % contador, end='')  # end = '' , alinhou as coisas, sem ele seria na vertical
    fatorial *= contador
    contador -= 1
print("1 = ",round(fatorial,2))
# round(fatorial) ou round(factorial,None) faz o mesmo, já com numero no lugar diz quantos numero vai mostrar apos a
# virgula. o mesmo serve pro print(f"{contador:,.2f}")
#
# todos os comandos acima fazem a mesma coisa, isso é apenas uma questão de gosto, escolher um deles.

# os comandos ocultos do python são confusos mas eu vou tentar te explicar
# esses pequenos e velhos comandos secretos...

# -esses são os importantes: %s = str; %d = int; %f = float.
# ja o resto... é confuso.
# _esses tem o mesmo resultado dos principais.. %r=float; %u=int(sem arredondar); %i=int(sem arredondar); %a=float;
# mas o %g deixa apenas aparecer 2 zeros0 apos a virgula.ou seja ele é um pouco melhor;
