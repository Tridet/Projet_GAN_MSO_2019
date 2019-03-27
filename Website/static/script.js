
function generateImage() {
    var description = document.getElementById('description').value
    document.getElementById('resultDescription').innerHTML = description

    var mode = getMode()
    var model = getModel()
    var object = getObject()
    var clsOption = getClsOption()

    var imageCount = 12

    // Delete previous results
    var results = document.getElementById('result')
    while (results.firstChild) {
        results.removeChild(results.firstChild);
    }
    // Create img empty elements
    for(let i = 0; i < imageCount ; i++){
        let img = document.createElement("img")
        img.id = 'resultImg' + i
        document.getElementById('result').appendChild(img)
    }
    if (mode === 'classic'){
        document.getElementById('resultDescription2').innerHTML = ''
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
    } else {
        var description2 = document.getElementById('description2').value
        document.getElementById('resultDescription2').innerHTML = description2
        getInterpolatedEmbeddings(description, description2)
    }
    
}


function getMode(){
    return getRadioValue('mode-choice', 'classic')
}

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

function getRandomDescription(elementID){
    let object = getObject()
    let url = '/random-description?object=' + object
    httpGetAsync(url, (description) => {
        document.getElementById(elementID).value = description
    })
}

function getInterpolatedEmbeddings(description1, description2){
    let object = getObject()
    let url = '/interpolated-embeddings?description1=' + description1 +
                '&description2=' + description2 +
                '&object=' + object
    httpGetAsync(url, embeddings => {
        generateImageFromEmbeddings(embeddings)
    })
}

function generateImageFromEmbeddings(embeddings){
    var model = getModel()
    var object = getObject()
    var clsOption = getClsOption()
    // Write new src for each image
    embeddings = JSON.parse(embeddings)
    for(let i = 0; i < embeddings.length ; i++){
        let img = document.getElementById('resultImg' + i)
        img.src = "/generateFromEmbedding?embedding=" + embeddings[i] +
                    "&model=" + model +
                    "&object=" + object +
                    "&cls=" + clsOption +
                    "&i=" + i + // Used to get different images (avoid cache)
                    "&time=" + new Date().getTime() // This is used as a cache breaker
    }
}


function httpGetAsync(theUrl, callback){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function changeMode(){
    let mode = getMode()
    let description2Container = document.getElementById('description2Container')
    if (mode === 'interpolated'){
        description2Container.style = 'display: flex;'
    } else {
        description2Container.style = 'display: none;'
    }
}


var classicModeRadio = document.getElementById('mode1')
classicModeRadio.addEventListener('change', changeMode)
var interpolatedModeRadio = document.getElementById('mode2')
interpolatedModeRadio.addEventListener('change', changeMode)

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







