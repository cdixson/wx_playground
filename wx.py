import json, requests, mysql.connector, time

from datetime import date
from time import sleep
from datetime import datetime

#connect to the database
mydb = mysql.connector.connect(user='{user}', 
	password='{pwd}',
	host='{host}',
	database='{db}')
             
while True:                 

	try:
		r = requests.get("http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon=-{lon}&APPID={ID}")

		data = r.json()

		humidity = (data['main']['humidity'])
		
		tempKelvin = (data['main']['temp'])
		tempCelcius = tempKelvin - 273.15
		tempFarenheit = (tempCelcius * 1.8000) + 32.00
		tempFarenheit = "{:.1f}".format(tempFarenheit)

		now = datetime.now()
		print (now.strftime("%Y-%m-%d %H:%M"))
		print (data['dt']) #timestamp
		print (tempFarenheit) #temp in F
		print (humidity) #humidity
	
		mycursor = mydb.cursor()

		sql = "INSERT INTO temperature (updated, tempF, humidity) VALUES (%s, %s, %s)"
		val = (data['dt'], tempFarenheit, humidity)
		
		mycursor.execute(sql, val)
		
		mydb.commit()
		
		print(mycursor.rowcount, "record inserted.")
		print("---------------------------------")

	except requests.exceptions.RequestException as e:    
		print ('cannot connect')
    
	time.sleep(600) #10 min