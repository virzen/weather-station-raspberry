import psycopg2
import datetime
from time import sleep
from requests import get


SLEEP_TIME = 1
CITY_ID = '7531836' # Poznan
OPENWEATHER_APPID = '***REMOVED***'
#FILE_NAME = './t1'
FILE_NAME = '/home/pi/stacja/t1'


def getTempFromFile(file):
  lines = file.readlines()
  temp = int(lines[1].split()[-1][2:]) / 1000
  return temp


conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, password=DBPASS)
cursor = conn.cursor()

def loop():
  while True:
    payload = { 'id': CITY_ID, 'appid': OPENWEATHER_APPID, 'units': 'metric' }
    req = get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    #print(req.url)
    output = req.json()
    apiTemp = output['main']['temp']

    f = open(FILE_NAME, "r")
    sensorTemp = getTempFromFile(f)
    f.close()

    # TODO: save api temp to db
    cursor.execute("INSERT INTO readings (sensor,api) VALUES (%s,%s)", [sensorTemp, apiTemp])
    conn.commit()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now, " saved sensor temp ", str(sensorTemp), " and api temp ", str(apiTemp))

    sleep(SLEEP_TIME)


try:
  loop()
except KeyboardInterrupt:
  cursor.close()
  conn.close()
finally:
  cursor.close()
  conn.close()
