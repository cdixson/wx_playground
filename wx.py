import json, requests

try:
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=41.865&lon=-71.490")
	data = r.json()

	tempKelvin = (data['main']['temp'])
	tempCelcius = tempKelvin - 273.15
	tempFarenheit = (tempCelcius * 1.8000) + 32.00
	
	theTime = (data['dt'])
	print theTime

	print tempFarenheit

except requests.exceptions.RequestException as e:    
    print "cannot connect"