
function generate_image() {
    var description = document.getElementById('description').value
    var model = ''
    var radios = document.getElementsByName('model-choice')
    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            model = radios[i].value
            break
        }
    }

    if (document.getElementById('result').childElementCount === 0) {
        var img = document.createElement("img")
        img.src = "/generate?description=" + description + "&model=" + model
        img.id = 'resultImg'
        document.getElementById('result').appendChild(img)

        var p = document.createElement("p")
        p.innerHTML = description
        p.id = 'resultDescription'
        document.getElementById('result').appendChild(p)
    } else {
        document.getElementById('resultImg').src = "/generate?description=" + description + "&model=" + model
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





