from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):

    locationDict = {
	'1 a':1,
        '1 b':2,
        '1 c':3,
        '2 a':4,
        '2 b':5,
        '2 c':6,
        '3 a':7,
        '3 b':8,
        '3 c':9,
	'1A':1,
	'1B':2,
	'1C':3,
	'2A':4,
	'2B':5,
	'2C':6,
	'3A':7,
	'3B':8,
	'3C':9,
	'1 alpha': 1,
	'1 bravo': 2,
	'1 charlie': 3,
        '1 Charlie': 3,
	'2 alpha': 4,
	'2 bravo': 5,
	'2 charlie':6,
        '2 Charlie': 6,
        '3 alpha': 7,
        '3 bravo': 8,
        '3 charlie':9,
        '3 Charlie':9,
	'grid':10,
	'the grid':10,
	'the cross':11,
	'cross':11,
	'the ex':12,
	'ex':12,
	'the square':13,
	'square':13,
	'the diamond':14,
	'diamond':14,
	'row 1':15,
	'row 2':16,
	'row 3':17,
	'column 1':18,
	'column 2':19,
	'column 3':20,
	'the corners':21,
	'corners':21,
	'the fan':22,
        'fan': 22,
	'the light':23,
        'light': 23,
	'the power strip':24,
        'power strip': 24
    }

    targetPin = locationDict[location]
    if targetPin == 22 or targetPin == 23 or targetPin == 24:
   	 GPIO.setup(targetPin, GPIO.OUT)
   	 if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
   	 if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)

    if targetPin == 1 or targetPin == 2 or targetPin ==3:
    	GPIO.setup(targetPin, GPIO.OUT)
	if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
        if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)

    if targetPin == 4 or targetPin == 5 or targetPin ==6:
        GPIO.setup(targetPin, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
        if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)

    if targetPin == 7 or targetPin == 8 or targetPin ==9:
        GPIO.setup(targetPin, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
        if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)
    
    if targetPin == 10:
	GPIO.setup(1, GPIO.OUT)
	GPIO.setup(2, GPIO.OUT)
	GPIO.setup(3, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(5, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)

        if status in ['off', 'low']:        GPIO.output(1, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(2, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(3, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(4, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(5, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(6, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(7, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(8, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(9, GPIO.LOW)


    if targetPin == 11:
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(5, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(2, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(4, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(5, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(6, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(8, GPIO.LOW)

    if targetPin == 12:
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(5, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)
        if status in ['off','low']:         GPIO.output(1, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(3, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(5, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(7, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(9, GPIO.LOW)

    if targetPin == 13:
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)

        if status in ['off', 'low']:        GPIO.output(1, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(2, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(3, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(4, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(6, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(7, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(8, GPIO.LOW)
        if status in ['off', 'low']:        GPIO.output(9, GPIO.LOW)

    if targetPin == 14:
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(2, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(4, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(6, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(8, GPIO.LOW)

    if targetPin == 15:
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(1, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(2, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(3, GPIO.LOW)

    if targetPin == 18:
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(1, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(4, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(7, GPIO.LOW)

    if targetPin == 16:
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(4, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(5, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(4, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(5, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(6, GPIO.LOW)

    if targetPin == 17:
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(7, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(8, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(9, GPIO.LOW)

    if targetPin == 19:
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(2, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(5, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(8, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(2, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(5, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(8, GPIO.LOW)

    if targetPin == 20:
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(6, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(3, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(6, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(9, GPIO.LOW)

    if targetPin == 21:
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(9, GPIO.OUT)
        if status in ['on', 'high']:        GPIO.output(1, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(3, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(7, GPIO.HIGH)
        if status in ['on', 'high']:        GPIO.output(9, GPIO.HIGH)

        if status in ['off','low']:         GPIO.output(1, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(3, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(7, GPIO.LOW)
        if status in ['off','low']:         GPIO.output(9, GPIO.LOW)

    return statement('Turning {} {}!'.format(location, status))

@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})
def gpio_control(status, pin):

        try:
                pinNum = int(pin)
        except Exception as e:
                return statement('Pin number not valid.')

        GPIO.setup(pinNum, GPIO.OUT)

        if status in ['on', 'high']: GPIO.output(pinNum, GPIO.HIGH)
        if status in ['off', 'low']: GPIO.output(pinNum, GPIO.LOW)


        #if pinNum == 5 or pinNum == 6 or pinNum == 26 or pinNum == 27:
        #       if status in ['on', 'high']: GPIO.output(pinNum, GPIO.LOW) #reversed pins on relay
        #       if status in ['off', 'low']: GPIO.output(pinNum, GPIO.HIGH)
        #else:
        #       if status in ['on', 'high']: GPIO.output(pinNum, GPIO.HIGH)
        #       if status in ['off', 'low']: GPIO.output(pinNum, GPIO.LOW)

        return statement('Turning pin {} {}'.format(pin, status))

if __name__ == '__main__':
        port = 5000  #the custom port you want, 5000 must be open/or port forward from the router
        app.run(host='localhost', port = port)

