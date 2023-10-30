# Exemplo de loop com LDR
from ponte import conectar, configurar_pino, alterar_estado_pino, ler_porta_analogica

conectar('COM3')
configurar_pino(9, 'saida')

while True:
    luz = ler_porta_analogica()
    if (luz > 550):
        print('LUZ DEMAIS!!!')
        break
    elif (luz > 400):
        print('CUIDADO, LUZ!!!')
    elif (luz > 300):
        print('MUITA LUZ')
    else:
        print('POUCA LUZ')
