const express = require('express')
const path = require('path')
const { Client } = require('pg')

const app = express()
app.get('/data', (req, res) => {
  const client = new Client()
  client.connect()

  client.query(`
    SELECT date as date, sensor as sensor, api as api
    FROM readings
    WHERE date >= NOW() - '1 day'::INTERVAL
  `, (err, queryRes) => {

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
  })
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
