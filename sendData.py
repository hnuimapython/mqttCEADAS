from sense_hat import SenseHat
import requests
from random import randint
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("85.119.83.194", 1883, 60)

client.loop_start()
sense = SenseHat()

while True:
    temp = sense.get_temperature()
    print("Temperatur:  %s C" % temp)
    time.sleep(2)
    ok = client.publish("ima5/temp", temp)
    break
