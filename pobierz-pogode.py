from os.path import join, dirname
from os import environ
import psycopg2
import datetime
from time import sleep
from requests import get
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SLEEP_TIME = int(environ.get('SLEEP_TIME'))
CITY_ID = int(environ.get('CITY_ID'))
FILE_NAME = environ.get('SENSOR_OUTPUT_FILENAME')
OPENWEATHER_APPID = environ.get('OPENWEATHER_APPID')
PGUSER = environ.get('PGUSER')
PGDATABASE = environ.get('PGDATABASE')
PGPASSWORD = environ.get('PGPASSWORD')


def getTempFromFile():
  file = open(FILE_NAME, 'r')
  lines = file.readlines()
  temp = int(lines[1].split()[-1][2:]) / 1000
  file.close()
  return temp

def getTempFromApi():
  payload = { 'id': CITY_ID, 'appid': OPENWEATHER_APPID, 'units': 'metric' }
  req = get('http://api.openweathermap.org/data/2.5/weather', params=payload)
  output = req.json()
  temp = output['main']['temp']
  return temp

def saveTempsToDb(sensorTemp, apiTemp):
  conn = psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD)
  cursor = conn.cursor()
  cursor.execute('INSERT INTO readings (sensor,api) VALUES (%s,%s)', [sensorTemp, apiTemp])
  conn.commit()
  cursor.close()
  conn.close()

def log(sensorTemp, apiTemp):
  now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print(now, ' saved sensor temp ', str(sensorTemp), ' and api temp ', str(apiTemp))


while True:
  apiTemp = getTempFromApi()
  sensorTemp = getTempFromFile()

  saveTempsToDb(sensorTemp, apiTemp)
  log(sensorTemp, apiTemp)

  sleep(SLEEP_TIME)
