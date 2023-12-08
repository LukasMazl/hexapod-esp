import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(1, sda=Pin(4), scl=Pin(16))  # Correct I2C pins for RP2040

pca = PCA9685(i2c)
servo7 = Servo(pca.channels[1])

pca.frequency = 50

SERVO_SLEEPING_TIME = 1

class Leg:
    def __init__(self, min, max, servo, reversed=False):
        self._min = min
        self._max = max
        self._servo = servo
        self._reversed = reversed

    def go_up(self):
        if self._reversed:
            self._servo.angel = self._min
        else:
            self._servo.angel = self._max
        time.sleep(SERVO_SLEEPING_TIME)

    def go_down(self):
        if self._reversed:
            self._servo.angel = self._min
        else:
            self._servo.angel = self._max
        time.sleep(SERVO_SLEEPING_TIME)
