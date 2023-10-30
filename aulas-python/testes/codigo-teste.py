from ponte import ler_quantidade_de_luz, ler_distancia, interruptor, conectar
from time import sleep

conectar('COM4')

while (1):
    luz = ler_quantidade_de_luz()
    distancia = ler_distancia()
    print('luz', luz)
    print('distancia(cm)', distancia)

    if (distancia > 30):
        interruptor(True)
    else:
        interruptor(False)

    sleep(1)
