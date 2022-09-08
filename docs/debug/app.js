const express = require('express');
const app = express();

const PORT = process.argv[2] || 8080;
const HOST =  process.argv[3] || '0.0.0.0';

app.get("/", function (req, res) {
    res.sendFile(__dirname + '/static/index.html')
});

app.listen(PORT, HOST);

console.log(`Running app on http://${HOST}:${PORT}`);