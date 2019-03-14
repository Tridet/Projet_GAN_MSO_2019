
function generate_image() {
    var description = document.getElementById('description').value
    var model = ''
    var model_radios = document.getElementsByName('model-choice')
    for (var i = 0, length = model_radios.length; i < length; i++) {
        if (model_radios[i].checked) {
            model = model_radios[i].value
            break
        }
    }

    var object = ''
    var object_radios = document.getElementsByName('object-choice')
    for (var i = 0, length = object_radios.length; i < length; i++) {
        if (object_radios[i].checked) {
            object = object_radios[i].value
            break
        }
    }

    if (document.getElementById('result').childElementCount === 0) {
        var img = document.createElement("img")
        img.src = "/generate?description=" + description + "&model=" + model + "&object=" + object
        img.id = 'resultImg'
        document.getElementById('result').appendChild(img)

        var p = document.createElement("p")
        p.innerHTML = description
        p.id = 'resultDescription'
        document.getElementById('result').appendChild(p)
    } else {
        document.getElementById('resultImg').src = "/generate?description=" + description + "&model=" + model + "&object=" + object
        document.getElementById('resultDescription').innerHTML = description
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





