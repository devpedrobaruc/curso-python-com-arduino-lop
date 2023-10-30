from ponte import ler_quantidade_de_luz, ler_distancia, interruptor, conectar, potencia_motor
from time import sleep

conectar('COM4')

while (1):
    luz = ler_quantidade_de_luz()
    distancia = ler_distancia()

    if (distancia > 100):
        distancia = 100

    print(100-distancia)
    potencia_motor(100-int(distancia))
