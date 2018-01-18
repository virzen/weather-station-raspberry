const express = require('express')
const path = require('path')

const { Client } = require('pg')

const app = express()
const client = new Client()

client.connect()

app.get('/data', (req, res) => {
  client.query('SELECT $1::text as message', ['Hello world!'])
    .then((err, res) => {
      console.log(err ? err.stack : res.rows[0].message) // Hello World!
      client.end()
    })
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/index.html'));
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))
