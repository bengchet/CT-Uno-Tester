import os
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define pin for SW and LED
SW0 = 10
LED0_GREEN = 9
LED0_RED = 11

SW1 = 17
LED1_GREEN = 27
LED1_RED = 22

SW2 = 2
LED2_GREEN = 3
LED2_RED = 4

# Set push button as input pull up
GPIO.setup(SW0, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(SW1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, GPIO.PUD_UP)

# Set LED as output
GPIO.setup(LED0_GREEN, GPIO.OUT)
GPIO.setup(LED0_RED, GPIO.OUT)
GPIO.setup(LED1_GREEN, GPIO.OUT)
GPIO.setup(LED1_RED, GPIO.OUT)
GPIO.setup(LED2_GREEN, GPIO.OUT)
GPIO.setup(LED2_RED, GPIO.OUT)

# At initial state turn off all LED
GPIO.output(LED0_GREEN, GPIO.HIGH)
GPIO.output(LED0_RED, GPIO.HIGH)
GPIO.output(LED1_GREEN, GPIO.HIGH)
GPIO.output(LED1_RED, GPIO.HIGH)
GPIO.output(LED2_GREEN, GPIO.HIGH)
GPIO.output(LED2_RED, GPIO.HIGH)

# Test all LED by create simple blink
GPIO.output(LED0_GREEN, GPIO.LOW)
GPIO.output(LED1_GREEN, GPIO.LOW)
GPIO.output(LED2_GREEN, GPIO.LOW)
time.sleep(0.1)
GPIO.output(LED0_GREEN, GPIO.HIGH)
GPIO.output(LED1_GREEN, GPIO.HIGH)
GPIO.output(LED2_GREEN, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(LED0_RED, GPIO.LOW)
GPIO.output(LED1_RED, GPIO.LOW)
GPIO.output(LED2_RED, GPIO.LOW)
time.sleep(0.1)
GPIO.output(LED0_RED, GPIO.HIGH)
GPIO.output(LED1_RED, GPIO.HIGH)
GPIO.output(LED2_RED, GPIO.HIGH)

time.sleep(1)

# Turn ON LED0 green
GPIO.output(LED0_GREEN, GPIO.LOW)

os.chdir('/home/pi')

try:
  while True:
    if GPIO.input(SW0) == 0:
      GPIO.output(LED0_GREEN, GPIO.HIGH)
      GPIO.output(LED1_GREEN, GPIO.HIGH)
      GPIO.output(LED2_GREEN, GPIO.HIGH)
      GPIO.output(LED0_RED, GPIO.LOW)
      os.system('sudo shutdown -h now')

    elif GPIO.input(SW1) == 0:
      GPIO.output(LED1_GREEN, GPIO.HIGH)
      GPIO.output(LED2_GREEN, GPIO.HIGH)
      GPIO.output(LED1_RED, GPIO.LOW)
      os.system('sudo avrdude -p atmega328p -C /home/pi/avrdude_gpio.conf -c pi_1 -v -U flash:w:optiboot_atmega328.hex:i -U efuse:w:0x05:m -U hfuse:w:0xde:m -U lfuse:w:0xff:m')
      os.chdir('/home/pi/RunningLight')
      os.system('make upload')
      os.chdir('/home/pi')
      GPIO.output(LED1_RED, GPIO.HIGH)
      GPIO.output(LED1_GREEN, GPIO.LOW)

    elif GPIO.input(SW2) == 0:
      GPIO.output(LED2_GREEN, GPIO.LOW)
      GPIO.output(LED2_RED, GPIO.LOW)
      os.system('sudo avrdude -p atmega328p -C /home/pi/avrdude_gpio.conf -c pi_1 -v -U flash:w:optiboot_atmega328.hex:i -U efuse:w:0x05:m -U hfuse:w:0xde:m -U lfuse:w:0xff:m')
      os.chdir('/home/pi/Blink')
      os.system('make upload')
      os.chdir('/home/pi')
      GPIO.output(LED2_RED, GPIO.HIGH)
      GPIO.output(LED2_GREEN, GPIO.LOW)

except KeyboardInterrupt:
  GPIO.cleanup()
