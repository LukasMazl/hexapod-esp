import time
from machine import Pin, I2C
from micropython_pca9685 import PCA9685
from micropython_pca9685 import Servo

i2c = I2C(1, sda=Pin(4), scl=Pin(16))  # Correct I2C pins for RP2040

pca = PCA9685(i2c)
servo7 = Servo(pca.channels[0])

pca.frequency = 50
# We sleep in the loops to give the servo time to move into position.

for i in range(90,180):
    servo7.angle = i
    time.sleep(0.03)
for i in range(90, 180):
    servo7.angle = 180 - i
    time.sleep(0.03)

# You can also specify the movement fractionally.
fraction = 0.0
while fraction < 1.0:
    servo7.fraction = fraction
    fraction += 0.01
    time.sleep(0.06)

pca.deinit()