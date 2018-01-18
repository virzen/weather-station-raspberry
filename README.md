# Weather station

## Install
Create a database:
```
intidb <file> -E utf8
psql -d stacja < dump.sql

Install server:
```
npm install
```

Install python dependencies:
```
pip3 install -r requirements.txt
```

Copy and fill `.env`:
```
cp .env.sample .env
# fill .env
```

## Run
```
npm start
```
