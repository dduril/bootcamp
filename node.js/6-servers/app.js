var express = require("express");
var cors = require("cors");
var bodyParser = require("body-parser");
var app = express();

var movies = [
    {
        Title: "The Phantom Menace",
        Runtime: 133,
        Year: 1999
    },{
        Title: "Attack of the Clones",
        Runtime: 142,
        Year: 2002
    },{
        Title: "Revenge of the Sith",
        Runtime: 140,
        Year: 2005
    },{
        Title: "A New Hope",
        Runtime: 123,
        Year: 1977
    },{
        Title: "The Empire Strikes Back",
        Runtime: 129,
        Year: 1980
    },{
        Title: "Return of the Jedi",
        Runtime: 136,
        Year: 1983
    },{
        Title: "Force Awakens",
        Runtime: 135,
        Year: 2015
    } 
];

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(function(req, res, next) {
    console.log(`${req.method} request for '${req.url}' - ${JSON.stringify(req.body)}`);
    next(); 
});

app.use(express.static("./public"));

app.use(cors());

app.get("/movie-api", function(req, res) {
    res.json(movies); 
});

app.listen(3000);

console.log("Express app running on port 3000");

module.exports = app;