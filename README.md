# Streamdeck Caseiro V1

Este projeto é um Stream Deck caseiro baseado em Raspberry Pi Pico e CircuitPython, desenvolvido especificamente para interagir com o software EXP Soundboard (Ou similar). O dispositivo utiliza um display OLED SH1107 de 128x128 pixels como interface visual e botões físicos para controle, permitindo acionar efeitos sonoros e outras funções através do envio de comandos de teclado numérico ao computador.

## Funcionalidades

- **Navegação entre mensagens**: O usuário pode navegar entre diferentes mensagens usando um botão de toque.
- **Envio de comandos de teclado**: Ao confirmar uma seleção, o projeto envia um comando de teclado correspondente à mensagem exibida.
- **Feedback sonoro**: O projeto emite sons para confirmar ações, como navegação e envio de comandos.

## Dependências

Este projeto requer as seguintes bibliotecas da Adafruit:

- adafruit_display_text
- adafruit_displayio_sh1107
- adafruit_hid
- busio
- displayio
- simpleio

###### Nota: As bibliotecas podem ser instaladas através do CircuitPython Bundle ou diretamente do repositório da Adafruit.

## Hardware Necessário
- 1x Raspberry Pi Pico ou similar
- 1x Display OLED SH1107 
- 2x Botões de toque TTP223 
- 1x Buzzer passivo
- Fios de conexão
- (Opcional) Impressora 3D para imprimir a caixa do Streamdeck.

## Como Executar

1. Carregue o circuito CircuitPython na sua placa Raspberry Pi Pico.
   - Para isso, baixe o firmware do CircuitPython para a sua placa e copie o arquivo `.uf2` para a unidade USB que aparece quando você conecta a placa.
   - Após isso, a unidade USB irá aparecer como `CIRCUITPY`.
2. Carregue o `code.py` e a pasta `lib` em sua placa compatível.
3. Execute o código e interaja com o Streamdeck Caseiro.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.