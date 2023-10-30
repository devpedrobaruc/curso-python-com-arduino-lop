from ponte import ler_distancia, conectar, potencia_motor, ler_porta_analogica
from time import sleep

conectar('COM3')

while (1):
    luz = ler_porta_analogica()
    distancia = ler_distancia()

    if (distancia > 100):
        distancia = 100

    print(100-distancia)
    potencia_motor(100-int(distancia))
