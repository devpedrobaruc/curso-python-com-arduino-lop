from ponte import ler_porta_analogica, ler_distancia, configurar_pino, conectar, alterar_estado_pino
from time import sleep

conectar('COM3')
configurar_pino(9, 'saida')

while (1):
    luz = ler_porta_analogica()
    distancia = ler_distancia()
    print('luz', luz)
    print('distancia(cm)', distancia)

    if (distancia > 30):
        alterar_estado_pino(9, True)
    else:
        alterar_estado_pino(9, False)

    sleep(1)
