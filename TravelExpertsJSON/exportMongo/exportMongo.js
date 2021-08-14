var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
const table = "packages";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("travelexperts");
  /*Return only the documents with the address "Park Lane 38":*/
  //var query = { address: "Park Lane 38" };
  dbo.collection(table).find().toArray(function(err, result) {
    if (err) throw err;
    //console.log(result);
	var fs = require('fs');

	fs.writeFile(table+'.json', JSON.stringify(result), function (err) {
	  if (err) throw err;
	  console.log('Saved!');
	});
    db.close();
  });
});
