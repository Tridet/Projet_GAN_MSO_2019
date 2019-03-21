
function generateImage() {
    var description = document.getElementById('description').value
    document.getElementById('resultDescription').innerHTML = description

    var model = getModel()
    var object = getObject()
    var clsOption = getClsOption()

    var imageCount = 12
    // Init results with empty images
    if (document.getElementById('result').childElementCount === 0) {
        // Create img empty elements
        for(let i = 0; i < imageCount ; i++){
            let img = document.createElement("img")
            img.id = 'resultImg' + i
            document.getElementById('result').appendChild(img)
        }
    }
    // Write new src for each image
    for(let i = 0; i < imageCount ; i++){
        let img = document.getElementById('resultImg' + i)
        img.src = "/generate?description=" + description +
                    "&model=" + model +
                    "&object=" + object +
                    "&cls=" + clsOption +
                    "&i=" + i + // Used to get different images (avoid cache)
                    "&time=" + new Date().getTime() // This is used as a cache breaker
    }
}


var input = document.getElementById('description');
// Execute a function when the user releases a key on the keyboard
input.addEventListener('keyup', function (event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        generate_image();
    }
});

function getModel(){
    return getRadioValue('model-choice', 'gan')
}

function getObject(){
    return getRadioValue('object-choice', 'flowers')
}

function getClsOption(){
    return getRadioValue('cls-choice', 'false')
}

function getRadioValue(radioName, default_value){
    var res = default_value
    var radios = document.getElementsByName(radioName)
    for (let i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            res = radios[i].value
            break
        }
    }
    return res
}

function getRandomDescription(){
    let object = getObject()
    let url = '/random-description?object=' + object
    httpGetAsync(url, (description) => {
        document.getElementById('description').value = description
    })
}

function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}





