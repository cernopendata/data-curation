var fs=require('fs');
var data=fs.readFileSync('cms_release_info.json');
var years=JSON.parse(data);
var data2=fs.readFileSync('run_ranges.json');
var run_eras=JSON.parse(data2);
const express = require("express");

var favicon = require('serve-favicon');
var path = require('path');


const app = express();

const cors=require('cors');

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`App started on PORT ${PORT}`);
  });


app.use(express.static('public'));
app.use(cors());
app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')))



app.get('/',welcome);
function welcome(request,response)
{
	let hostname=request.get('Host')
	console.log(request.get('Host'));
	var reply={
		usage: "Add a path, available paths: http://"+hostname+"/years and http://"+hostname+"/runeras",
		years: "use: /years/ to get all year info or: /years/<key> for a specific value",
		runeras: "use: /runeras/ to get all run era info or: /runeras/<key> for a specific value",
		queries: "Pass a query with: ?<akey>=<avalue>",
		example: "http://"+hostname+"/runeras/run_era?year=2015",
		output: "For year info, output=plain returns single values without square brackets"
	}
    response.send(reply);
}


app.get('/years/:mykey?',searchYear);
function searchYear(request,response)
{
	var key=request.params.mykey;
	var filters=request.query;
	var filtered_years = years;
	var output_value;

	for (var reqkey in filters) {
		if (reqkey == 'output')
		{
			output_value = filters[reqkey];
		}
		else
		{
			filtered_years = filtered_years.filter(a_year => a_year[reqkey] == filters[reqkey]);
		}
	}

	var reply;

	if (key)
	{
		// note that year.key won't work
		let keyvalues = filtered_years.map(year => year[key]);
		reply = keyvalues;
	}
	else
	{
		reply=filtered_years;
	}
	
    console.log(reply);

	// There are reasons to do this (i.e. to get CMSSW_5_3_32 instead of [ "CMSSW_5_3_32" ])
	// but this is probably not a good idea in general
	// adding a query parameter for output format: output=plain returns reply without square brackets
	if (reply.length == 1 && output_value == 'plain') 
	{
		if (typeof reply[0] == 'string') 
		{
			reply = String(reply[0]);
		}
		else
		{
			reply = reply[0];
		}
	}
	response.send(reply);
}

app.get('/runeras/:mykey?',searchEra);
function searchEra(request,response)
{
	var key=request.params.mykey;
	var filters=request.query;
	var filtered_eras = run_eras;
	
	for (var reqkey in filters) {
		filtered_eras = filtered_eras.filter(an_era => an_era[reqkey] == filters[reqkey]);
	}

	var reply;
	
	if (key)
	{
		// note that era.key won't work
		let keyvalues = filtered_eras.map(era => era[key]);
		reply = keyvalues;
	}
	else
	{
		reply=filtered_eras;
	}

    console.log(reply);
	response.send(reply);
}

