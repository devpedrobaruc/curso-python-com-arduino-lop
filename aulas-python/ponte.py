import serial
import serial.tools.list_ports
from time import sleep

connection: serial.Serial | None = None


def conectar(port) -> None:
    global connection
    connection = serial.Serial(port, 9600, timeout=None)
    sleep(2)


def ler_distancia() -> float:
    if (connection == None):
        return float(0)

    connection.write(b'1')
    data = connection.readline().decode()

    if (data == ''):
        return float(0)
    return float(data)


def ler_porta_analogica() -> float:
    if (connection == None):
        return float(0)

    connection.write(b'2')
    data = connection.readline().decode()

    if (data == ''):
        return float(0)
    return float(data)


def configurar_pino(pino: int, modo: str) -> None:
    if (connection == None):
        raise Exception('ERRO CONFIGURAR')

    if (modo != 'entrada' and modo != 'saida'):
        raise Exception('O modo só pode ser "entrada" ou "saida"')

    connection.write((b'3' if modo == 'entrada' else b'4') +
                     pino.to_bytes(1, 'little'))


def alterar_estado_pino(pino: int, estado: bool) -> None:
    if (connection == None):
        raise Exception('ERRO ESTADO')

    pino_byte = pino.to_bytes(1, 'little')
    estado_byte = b'1' if estado else b'0'
    connection.write(b'5'+pino_byte+estado_byte)


def potencia_motor(potencia: int) -> None:
    if (connection == None):
        raise Exception('ERRO MOTOR')

    connection.write(b'6'+potencia.to_bytes(1, 'little'))


if __name__ == '__main__':
    print([i.name for i in serial.tools.list_ports.comports()])
