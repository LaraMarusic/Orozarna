const express = require('express');
const fs = require('fs');

const app = express();

app.use(express.static('./public'));

app.get('/:id', function (req, res) {

    let id = req.params.id;

    let nid = "";
    for (let i = 0; i < id.length; i++) {
        if (i < id.length - 1) {
            nid += "'" + id[i] + "'" + ","
        } else {
            nid += "'" + id[i] + "'"
        }
    }
    nid += "";
    fs.readdir('./public/Slike', function (err, files) {
        console.log(nid);
        for (let file of files) {
            if (file.indexOf(nid) != -1) {
                console.log(file);
                res.json({ value: file });
            }
        }
    });
});

app.listen(8000);
