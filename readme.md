# Extenção LOP
## Utilizado na minha extensão de Logica de programação

## O intuito deste código é mostrar a programação em python em embarcados com placas que não suportam micropython para alunos do 8 ano, fazendo o aprendizado ser mais divertido. 

## Pinos utilizados(Arduino Uno):

- A0: Leitura analogica
- Pino 3: Controlador de esc

## Comandos seriais:

- '1': Faz a leitura do sensor ultrassonico

- '2': Faz a leitura analogica do pino definido no código

- '3', pino: Configura o pino como entrada

- '4', pino: Configura o pino como saída

- '5', pino, 'valor': Ativa a o pino caso valor seja '1', se receber qualquer outro valor ele desliga o pino

- '6', valor: A potencia do ESC será setada entre 0% e 100%, caso o valor enviado seja maior, ele limitará em 100%.

- 'r'(ou qualquer outro valor não listado): Ignora

## Métodos no python:

- conectar(portaSerial): Faz a conexão serial do arduino com o código em python
- ler_distancia(): Retorna a distancia do sensor ultrassonico
- ler_porta_analogica(): Retorna o valor lido na porta analogica
- configurar_pino(pino, modo:'saida'|'entrada'): Configura o pino como saída ou como entrada
- alterar_estado_pino(estado): Liga ou desliga o pino configurado como saída
- ler_pino(pino): Faz a leitura digital do pino configurado como entrada
- potencia_motor(potencia): Seta a potencia do motor entre 0% e 100%

### OBS: os arquivos com os metodos estão em: aulas-python/ponte.py

