# Exemplo de loop com LDR
from ponte import conectar, configurar_pino, alterar_estado_pino, ler_porta_analogica

conectar('COM3')
configurar_pino(9, 'saida')

while True:
    luz = ler_porta_analogica()
    if (luz > 550):
        alterar_estado_pino(9, False)
        print('LUZ DEMAIS!!!')
        break
    elif (luz > 400):
        alterar_estado_pino(9, False)
        print('CUIDADO, LUZ!!!')
        continue
    elif (luz > 300):
        print('MUITA LUZ')
    else:
        print('POUCA LUZ')

    alterar_estado_pino(9, True)
