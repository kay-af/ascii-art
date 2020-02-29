// Created by Afridi

var mDiv;
var jsonData;

onload = function () {
    var fileChooser = document.getElementById("file-chooser");
    fileChooser.onchange = function (evt) {
        pause();
        count = 0;
        var jsonFile = fileChooser.files[0];
        let reader = new FileReader();
        reader.readAsText(jsonFile);
        reader.onload = function (evt) {
            document.getElementById("file-name").innerHTML = "Loading file...";
        }
        reader.onloadend = function (evt) {
            console.log("File loaded");
            document.getElementById("file-name").innerHTML = jsonFile.name;
            jsonData = JSON.parse(reader.result); 
            mDiv = document.getElementById('player');
        }
        reader.onerror = alertError;
    };
};

var count = 0
var intId;

function play() {
    if(jsonData != null)
        intId = setInterval(repeater, 34);
}

function pause() {
    if(intId != null)
        clearInterval(intId);
}

function alertError() {
    stop();
    alert("Error loading file! Generate frames again");
    document.getElementById("file-name").innerHTML = "";
    jsonData = null;
}

function repeater() {
    try {
        mDiv.innerHTML = jsonData["frames"][count];
        count++;
        count = count % jsonData["meta"]["nFrames"];
    } catch (err) {
        alert("Invalid file");
        pause();
    }
}