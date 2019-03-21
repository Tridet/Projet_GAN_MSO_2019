
function generate_image() {
    var description = document.getElementById('description').value
    document.getElementById('resultDescription').innerHTML = description

    var model = 'gan'
    var model_radios = document.getElementsByName('model-choice')
    for (let i = 0, length = model_radios.length; i < length; i++) {
        if (model_radios[i].checked) {
            model = model_radios[i].value
            break
        }
    }

    var object = 'flowers'
    var object_radios = document.getElementsByName('object-choice')
    for (let i = 0, length = object_radios.length; i < length; i++) {
        if (object_radios[i].checked) {
            object = object_radios[i].value
            break
        }
    }

    var clsOption = 'false'
    var cls_radios = document.getElementsByName('cls-choice')
    for (let i = 0, length = cls_radios.length; i < length; i++) {
        if (cls_radios[i].checked) {
            clsOption = cls_radios[i].value
            break
        }
    }

    // Init results with empty images
    if (document.getElementById('result').childElementCount === 0) {
        // Create img empty elements
        for(let i = 0; i < 10 ; i++){
            let img = document.createElement("img")
            img.id = 'resultImg' + i
            document.getElementById('result').appendChild(img)
        }
    }
    // Write new src for each image
    for(let i = 0; i < 10 ; i++){
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





