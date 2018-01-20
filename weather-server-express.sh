#!/bin/bash
### BEGIN INIT INFO
# Provides:          weather-server-express
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Server for displaying weather station results
### END INIT INFO

USER=pi
DIR=/home/pi/stacja
LOG_FILE=/tmp/weather-server-express.log

case "$1" in
  start)
    (cd $DIR && sudo -u $USER npm start >$LOG_FILE 2>&1 &)
    ;;
  stop)
    pkill -u $USER -f node
    ;;
  *)
    echo "Usage: service weather-server-express {start|stop}"
    ;;
esac
