# Script em python para [Shield LoRaWAN Raspberry Pi](https://github.com/fox-iot/Send_CPU_Rpi_LoRaWAN_Shield_Fox/blob/main/doc/Shield_Lora_Foxiot.pdf) (desenvolvido por [Fox IoT](http://foxiot.com.br))

Esse Script proporciona interface entre hardware e software, composta por um chip LoRa [RFM95](http://www.hoperf.com/upload/rf/RFM95_96_97_98W.pdf)
operando na frequência de 915 MHz e três LEDs indicadores, sendo um de cor verde que indica power on e dois vermelhos de uso geral podendo ser configurados para indicar algum tipo de status do sistema.

## Para executar o script é necessário

- Instalar Python 3.x e Pip (Veja como instalar o python em [python.org](https://python.org)).
- Executar "pip install -r requirements.txt"
- Listar os packages, use "pip freeze"

- Executar o script "sudo python3 send_data_lorawan.py"

## Mapeamento de hardware

O mapeamento completo de pinos da BCM pode ser visto [aqui](https://github.com/fox-iot/Send_CPU_Rpi_LoRaWAN_Shield_Fox/blob/main/doc/Raspberry%20Pi%20GPIO%20Pins.png)

BCM 17 == Reset

BCM 23 == DIO0

BCM 24 == DIO1

BCM 18 == DIO2 (Não utilizado)

BCM 10 == MOSI

BCM 9 == MISO

BCM 11 == SCK

BCM 25 == SS

BCM 27 == LED1

BCM 22 == LED2
  
GND  == GND
  
3.3V  == +3.3V  

## Licença

O conteúdo está licenciado sob a licença MIT. Veja [License File](LICENSE) para mais informações.
