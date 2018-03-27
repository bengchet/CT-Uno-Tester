# CT-Uno-Tester
Tester for CT Uno
Maintained by Ng Beng Chet ([bengchet@cytron.io](mailto:bengchet@cytron.io))

## Installing on Raspberry Pi
- ```sudo apt-get install avrdude```
- ```sudo apt-get install arduino-mk```
- ```cd /home/pi```
- ```git clone https://github.com/CytronTechnologies/CT-Uno-Tester.git tester```
- ```sudo mv tester/* /home/pi/ && rm -rf tester```
- ```cat "python /home/pi/CTUnoTestJig.py &" >> /etc/rc.local```
- ```sudo reboot```

## References
- [Installation | Program an AVR or Arduino Using Raspberry Pi GPIO | Adafruit Learning System](https://learn.adafruit.com/program-an-avr-or-arduino-using-raspberry-pi-gpio-pins/installation)
