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
  - ![image](https://github.com/user-attachments/assets/dfeaf6ff-6cd0-455f-a155-2efe0cdec150)

- 1x Display OLED SH1107
   - ![image](https://github.com/user-attachments/assets/1cc898f1-1c55-486b-86fc-afa17049cca9)

- 2x Botões de toque TTP223
   - ![image](https://github.com/user-attachments/assets/876cb80c-0a57-419b-92b8-1d4877e8e10f)

- 1x Buzzer passivo
   - ![image](https://github.com/user-attachments/assets/5a85d628-f7b2-4b66-b1d0-ccc9257bdae8)

- Fios de conexão
   - ![image](https://github.com/user-attachments/assets/a177bd65-fbfb-4803-a4b6-e08f8aa0ed3d)

- (Opcional) Impressora 3D para imprimir a caixa do Streamdeck
   - ![image](https://github.com/user-attachments/assets/f148c923-f2f2-4a57-9ad8-8c0fb0e59408)


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
