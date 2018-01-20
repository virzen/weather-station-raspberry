#!/bin/bash
### BEGIN INIT INFO
# Provides:          weather-script
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script for getting and saving weather
### END INIT INFO

USER=pi
SCRIPT_FILE=/home/pi/stacja/get-weather.py
SCRIPT_FILENAME=`basename $SCRIPT_FILE`
LOG_FILE=/tmp/weather-script.log

case "$1" in
  start)
    sudo -u $USER $SCRIPT_FILE >$LOG_FILE 2>&1 &
    ;;
  stop)
    pkill -f $SCRIPT_FILENAME
    ;;
  *)
    echo "Usage: service weather-script {start|stop}"
    ;;
esac
