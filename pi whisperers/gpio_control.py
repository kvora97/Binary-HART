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
        'fan': 17,
        'light': 26,
	'power strip': 27
    }
	
    targetPin = locationDict[location]

    GPIO.setup(targetPin, GPIO.OUT)

    if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
    if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)

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
	#	if status in ['on', 'high']: GPIO.output(pinNum, GPIO.LOW) #reversed pins on relay
	#	if status in ['off', 'low']: GPIO.output(pinNum, GPIO.HIGH)
	#else:
	#	if status in ['on', 'high']: GPIO.output(pinNum, GPIO.HIGH)
	#	if status in ['off', 'low']: GPIO.output(pinNum, GPIO.LOW)

	return statement('Turning pin {} {}'.format(pin, status))

if __name__ == '__main__':
	port = 5000  #the custom port you want, 5000 must be open/or port forward from the router

		#app.run(host='192.168.100.1', port=port)
		#app.run(host='0.0.0.0', port=port)
		# app.run(host='127.0.0.1:4040', port=port) #Web Interface didn't work 
                #app.run(host='127.0.0.1', port=port)
		#app.run(host='192.168.0.20', port=port) #wlan0  inet (hopefully localhost)

		#app.run(host='100.80.241.153', port=port)
		#app.run(host='127.0.0.1', port = port)
	app.run(host='localhost', port = port)

