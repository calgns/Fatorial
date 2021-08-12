# o fatorial é um valor multiplicado por todos os numeros
# em ordem decrescente ate o N°1 tendo como ponto de partida o numero dado
# exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120;
# no python tem varias formas de se fazer uma coisa o que eu voe ensinar
# agora é uma das maneiras de como fazer um fatorial no python
def fatorial(numero):
    if numero == 1:
        return 1
    #veja que não é necessário o uso de else,
    # pois, apenas se numero for = 1 que vai retornar alguma coisa
    return numero * fatorial(numero - 1)
    #agora oque o ²return esta fazendo é pegar um numero e multiplicar pelo numero - 1
    # exemplo: 5 * (5 - 1)=4, ou seja, ele vai multiplicar 5 * 4. sempre um valor a menos;
