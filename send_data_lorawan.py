"""
Example for using the Shield Fox LoRa with Raspberry Pi and LoRaWAN
 
Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Lucas Maziero for Fox IoT (lucasmaziero@foxiot.com.br) (Adapted)
"""
import threading
import time
import subprocess
import busio
from digitalio import DigitalInOut, Direction, Pull
from random import randint
import board
# Import Adafruit TinyLoRa
from adafruit_tinylora.adafruit_tinylora import TTN, TinyLoRa
 
# TinyLoRa Configuration
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = DigitalInOut(board.D25)
irq = DigitalInOut(board.D23)
rst = DigitalInOut(board.D17)
 
# TTN Device Address, 4 Bytes, MSB
devaddr = bytearray([0xFF, 0xFF, 0xFF, 0xFF])
# TTN Network Key, 16 Bytes, MSB
nwkey = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])

app = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
# Initialize ThingsNetwork configuration
ttn_config = TTN(devaddr, nwkey, app, country='AU')
# Initialize lora object
lora = TinyLoRa(spi, cs, irq, rst, ttn_config, 0)
#TinyLoRa._tx_random = 15
# Select spreading factor
lora.set_datarate("SF10BW125")
# 2b array to store sensor data
data_pkt = bytearray(2)
# time to delay periodic packet sends (in seconds)
data_pkt_delay = 10.0

def send_pi_data_periodic():
    threading.Timer(data_pkt_delay, send_pi_data_periodic).start()
    print("Sending periodic data...")
    # read the raspberry pi cpu load
    cmd = "top -bn1 | grep load | awk '{printf \"%.1f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    CPU = float(CPU)
    send_pi_data(CPU)
 
def send_pi_data(data, ch_first = 0, ch_last = 7):

    # Encode float as int
    data = int(data * 100)
    # Encode payload as bytes
    data_pkt[0] = (data >> 8) & 0xff
    data_pkt[1] = data & 0xff
    # Send data packet
    lora.set_channel(randint(ch_first, ch_last))
    lora.send_data(data_pkt, len(data_pkt), lora.frame_counter, timeout = 5)
    lora.frame_counter += 1
    print('Data sent!')
    print('Counter: ', lora.frame_counter)
    #time.sleep(0.5)

send_pi_data_periodic()