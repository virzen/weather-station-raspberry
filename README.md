# Weather station

## Install
### DB
Create a database:
```
intidb <file> -E utf8

psql
=# CREATE DATABASE stacja;
<Ctrl-D>

psql -d stacja < dump.sql
=# CREATE USER pi WITH PASSWORD '<password>';
=# GRANT USAGE, SELECT ON readings TO pi;
=# GRANT USAGE, SELECT ON SEQUENCE readings_id_seq TO pi;
```

### Express server
Install server:
```
npm install
```

### Script
Install python dependencies:
```
pip3 install -r requirements.txt
```

### .env
Copy and fill `.env`:
```
cp .env.sample .env
vim .env
```

## Run on boot
```
# change neccessary variables in services/weather-{script|server-express} files
# add services
# usage: sudo service weather-{scripts|server-express} {start|stop|status}
sudo ln -v <project-dir>/services/weather-script.sh /etc/init.d/weather-script
sudo ln -v <project-dir>/services/weather-server-express.sh /etc/init.d/weather-server-express

# run services at boot
sudo update-rc.d weather-script defaults
sudo update-rc.d weather-server-express defaults
```

## Use Grafana (on Raspberry Pi Zero W)
### Install some packages and add the bintray pubkey to the apt keyring:
```
sudo apt-get install apt-transport-https curl
curl https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -
```

### Update your apt source
```
echo "deb https://dl.bintray.com/fg2it/deb-rpi-1b jessie main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```

### Install
```
sudo apt-get update
sudo apt-get install grafana
```

For more see: https://www.circuits.dk/install-grafana-influxdb-raspberry/#

### Start at boot
Check if `/etc/systemd/system/grafana-server.service` is a correct link to `/lib/systemd/system/grafana-server.service`.

If not, create `/lib/systemd/system/grafana-server.service` the source file is [here](https://github.com/grafana/grafana/blob/master/packaging/deb/systemd/grafana-server.service).

Then create the correct link:
```
sudo ln -s /lib/systemd/system/grafana-server.service /etc/systemd/system/grafana-server.service
```

Then enable grafana-server;
```
sudo systemctl enable grafana-server
```

Then start grafana-server
```
sudo systemctl start grafana-server
```

Via https://askubuntu.com/a/859739.
