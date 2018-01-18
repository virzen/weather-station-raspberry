import psycopg2
import datetime
from time import sleep
from requests import get


SLEEP_TIME = 1
CITY_ID = '7531836' # Poznan
OPENWEATHER_APPID = '***REMOVED***';


def getTempFromFile(file):
  lines = file.readlines()
  temp = int(lines[1].split()[-1][2:]) / 1000
  return temp


conn = psycopg2.connect("dbname=virzen user=virzen")
cursor = conn.cursor()

def loop():
  while True:
    payload = { 'id': CITY_ID, 'appid': OPENWEATHER_APPID, 'units': 'metric' }
    req = get('http://openweathermap.org/data/2.5/weather', params=payload)
    print(req.url)
    print(req.json())
    # TODO: get temp data
    apiTemp = 123

    f = open("./t1", "r")
    sensorTemp = getTempFromFile(f)
    f.close()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # TODO: save api temp to db
    cursor.execute("INSERT INTO readings (sensor) VALUES (%s)", [sensorTemp])
    conn.commit()

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
