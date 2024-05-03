
const express = require("express");
const routes = require("./routes/start");
const app = express();
const cors = require("cors");
const ip = require("ip");
const ipAddr= ip.address();
const port = 3000;
const bodyParser = require("body-parser");

let lastHouseVisited = "";
app.use(cors());


//app.use(express.json());

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use("/", routes);

app.get("/", (req, res) => {
  res.json({message: lastHouseVisited});
})
app.post("/", (req, res) => {
  lastHouseVisited = req.body.house;
  res.json({message: lastHouseVisited});
});
//app.use(express.static("../front"))


app.listen(3000, () => {
  console.log("Server run: http://" + ipAddr + ":3000");
});

