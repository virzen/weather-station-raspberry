sudo ln -vf `pwd`/services/weather-script.sh /etc/init.d/weather-script
sudo ln -vf `pwd`/services/weather-server-express.sh /etc/init.d/weather-server-express

sudo update-rc.d weather-script default
sudo update-rc.d weather-server-express default
