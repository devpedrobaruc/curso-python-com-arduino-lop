# Exemplo de loop com LDR
from ponte import conectar, configurar_pino, alterar_estado_pino, ler_porta_analogica

conectar('COM3')
configurar_pino(9, 'saida')

luz = ler_porta_analogica()
while luz < 500:
    luz = ler_porta_analogica()

    if (luz > 300):
        print('MUITA LUZ')
    else:
        print('POUCA LUZ')

print('LUZ DEMAIS!!!')
