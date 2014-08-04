import json, requests, datetime

try:
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=41.865519&lon=-71.491376")

	data = r.json()

	print (r.headers['content-type'])

	tempKelvin = (data['main']['temp'])

	tempCelcius = tempKelvin - 273.15
	tempFarenheit = (tempCelcius * 1.8000) + 32.00
	
	print(datetime.datetime.fromtimestamp(int(data['dt']))).strftime('%Y-%m-%d %H:%M:%S %Z%z')

	print (data['name'])
	print tempFarenheit

except requests.exceptions.RequestException as e:    
    print "cannot connect"

#location
#temp (increasing or decreasing in last hour, icon up/down)
#barometric pressure
#current conditions (icon)
#alert