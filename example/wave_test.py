import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(1, sda=Pin(4), scl=Pin(16))  # Correct I2C pins for RP2040

pca = PCA9685(i2c)
servos = []
for channel in pca.channels:
    servos.append(Servo(channel))

pca.frequency = 50

def wave(servo0, servo1):
    for i in range(100):
        servo0.angle = 90
        time.sleep(1)
        servo0.angle = 180
        time.sleep(1)
        servo1.angle = 0
        time.sleep(1)
        servo1.angle = 180
        time.sleep(1)
