const async = require('async');
const express = require('express');
const fs = require('fs');
const request = require('request');
const constants = require('./constants').constants;

var app = express();

var apiExtractor = {
    DEFAULT_DIR: 'dataset/',
    DEFAULT_PREFIX: '7656119',
    SUFFIXES: [],

};

app.get('/test', function(httpRequest, httpResponse) {
    // Variable
    const BASE_SUFFIX = 7961763992;
    temp_suffix = BASE_SUFFIX;

    for (var i = 0; i < 200000; i++) {
        temp_suffix = temp_suffix + 1;
        apiExtractor.SUFFIXES.push(temp_suffix);
    }

    getData();
});

function getData () {

    async.eachSeries(apiExtractor.SUFFIXES, function(suffix, next) {

        setTimeout(function() {
            console.log(suffix);


            const STEAM_ID = apiExtractor.DEFAULT_PREFIX + suffix;

            var url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/' +
                          'v0001/?key=' + constants.STEAMAPIKEY_GOLDY + '&steamid=' + STEAM_ID +'&format=json';

            request.get(url, function(error, steamHttpResponse, steamHttpBody) {
                //httpResponse.setHeader('Content-Type', 'application/json');
                //httpResponse.send(steamHttpBody);
                // console.log(steamHttpBody);

                var fileName = apiExtractor.DEFAULT_DIR + STEAM_ID + '.json';
                // console.log(steamHttpBody);

                if (steamHttpBody == '{\n\t"response": {\n\n\t}\n}') {
                    // do nothing
                    // callback();
                    next();
                } else {
                    fs.writeFile(fileName, steamHttpBody);
                    console.log('WROTE THE FILE! ', fileName);

                    //setTimeout(function() { }, 10000);
                    // callback();

                    next();
                }

            // if (steamHttpBody.response) {
            //     console.log('ahoo')
            // }

            
            });

            // next(); // don't forget to execute the callback!

         }, 1050);
        // console.log(SUFFIXES);
        

        // fs.readFile(__dirname + value, "utf8", function (err, data) {
        //     if (err) return callback(err);
        //     try {
        //           configs[key] = JSON.parse(data);
        //         } catch (e) {
        //           return callback(e);
        //         }
        //         callback();
        // })
    
    }, function (err) {
          if (err) console.error(err.message);
    });
}


app.listen(3000, function() {
    console.log('Server is now running at port 3000');
});