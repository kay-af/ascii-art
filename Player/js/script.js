// The json data that is currently loaded
var jsonData;
// The current frame number that is being shown
var count = 0;
// To keep track of the interval which will be used to call the repeater function repeatedly
var intId;

onload = function () {
    // Lets add listeners for our font sizer
    var fontSizer = document.getElementById("font-size");
    fontSizer.oninput = evt => {
        document.getElementById("player").style.fontSize = fontSizer.value + "px";
    };
    document.getElementById("player").style.fontSize = fontSizer.value + "px";
    
    // The file chooser API will help us to load outr file
    var fileChooser = document.getElementById("file-chooser");
    fileChooser.onchange = function (evt) {
        // Whenever the file changes, pause the current video first if already playing
        // Also set count to 0
        pause();
        count = 0;

        // Get our frames file
        var jsonFile = fileChooser.files[0];
        let reader = new FileReader();
        reader.readAsText(jsonFile);
        reader.onload = function (evt) {
            // Display loading text while loading
            document.getElementById("file-name").innerHTML = "Loading file...";
        }
        reader.onloadend = function (evt) {
            console.log("File loaded");
            // Show the file name in the top bar
            document.getElementById("file-name").innerHTML = jsonFile.name;
            jsonData = JSON.parse(reader.result); 
            // We are all set
        }
        // If error occurs, call the alert error function
        reader.onerror = alertError;
    };
};

function play() {
    // Called when we press play
    if(jsonData != null)
        intId = setInterval(repeater, 34);
    // repeater method is called every 34 ms
}

function pause() {
    // Paused when we press pause
    if(intId != null)
        clearInterval(intId);
}

// If an error occurrs, this method is called
function alertError() {
    alert("Error loading file! Generate frames again");
    document.getElementById("file-name").innerHTML = "";
    jsonData = null; // Set json data as null
}

// This method is responsible for playing the stuff
function repeater() {
    try {
        // Try to fetch the frame which is simple text
        document.getElementById('player').innerHTML = jsonData["frames"][count];
        // Next frame
        count++;
        // Set count = 0 once the end of frames have been reached
        count = count % jsonData["meta"]["nFrames"];
    } catch (err) {
        // If error occurs while reading, The file may have been corrupted.
        // Pause in this case
        alert("Invalid file");
        pause();
    }
}