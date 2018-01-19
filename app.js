const express = require('express')
const path = require('path')
const Client = require('pg').Client

const app = express()
app.get('/data', function (req, res) {
  console.log(new Date(), ': /data request')

  const client = new Client()
  client.connect()

  client.query(
    "SELECT date as date, sensor as sensor, api as api FROM readings WHERE date >= NOW() - '1 day'::INTERVAL",
    function (err, queryRes) {
      if (err) {
        console.log(err)
        res.status(500);
        res.json({ error: err })
      }
      else {
        const response = queryRes.rows
        res.json(response)
      }

      client.end()
    }
  );
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.listen(3000, function () { console.log('Listening on port 3000!') })
