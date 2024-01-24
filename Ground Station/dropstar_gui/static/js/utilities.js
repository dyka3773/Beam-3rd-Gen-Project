function setMotorStatus(motor, status){
    if (status == 0){
        $(motor).html("OFF")
        $(motor).removeClass()
        $(motor).addClass("text-danger")
    }
    else if (status == 1){
        $(motor).html("ON")
        $(motor).removeClass()
        $(motor).addClass("text-success")
    }
    else {
        $(motor).html(`Error  \t\t (${status})`)
        $(motor).removeClass()
        $(motor).addClass("text-warning")
        $(motor).addClass("text-dark")
    }
}

function setSoundCardStatus(soundCard, status){
    if (status == 0){
        $(soundCard).html("FINISHED")
        $(soundCard).removeClass()
        $(soundCard).addClass("text-danger")
    }
    else if (status == 1){
        $(soundCard).html("ON / IVED OFF")
        $(soundCard).removeClass()
        $(soundCard).addClass("text-primary") // This is the default color which is blue
    }
    else if (status == 2){
        $(soundCard).html("ON / IVED RECORDING")
        $(soundCard).removeClass()
        $(soundCard).addClass("text-success")
    }
    else {
        $(soundCard).html(`Error  \t\t (${status})`)
        $(soundCard).removeClass()
        $(soundCard).addClass("text-warning")
        $(soundCard).addClass("text-dark")
    }
}

function setCameraStatus(camera, status){
    if (status == 0){
        $(camera).html("FINISHED")
        $(camera).removeClass()
        $(camera).addClass("text-danger")
    }
    else if (status == 1){
        $(camera).html("ON / STANDBY")
        $(camera).removeClass()
        $(camera).addClass("text-primary")
    }
    else if (status == 2){
        $(camera).html("RECORDING")
        $(camera).removeClass()
        $(camera).addClass("text-success")
    }
    else {
        $(camera).html(`Error  \t\t (${status})`)
        $(camera).removeClass()
        $(camera).addClass("text-warning")
        $(camera).addClass("text-dark")
    }
}

function setLEDStatus(led, status){
    if (status == 0){
        $(led).html("OFF")
        $(led).removeClass()
        $(led).addClass("text-danger")
    }
    else if (status == 1){
        $(led).html("ON")
        $(led).removeClass()
        $(led).addClass("text-success")
    }
    else {
        $(led).html(`Error  \t\t (${status})`)
        $(led).removeClass()
        $(led).addClass("text-warning")
        $(led).addClass("text-dark")
    }
}

function setSignalStatus(element, status){
    if (status == false){
        $(element).html("OFF")
        $(element).removeClass()
        $(element).addClass("text-danger")
    }
    else if (status == true){
        $(element).html("ON")
        $(element).removeClass()
        $(element).addClass("text-success")
    }
    else {
        $(element).html(`Error  \t\t (${status})`)
        $(element).removeClass()
        $(element).addClass("text-warning")
        $(element).addClass("text-dark")
    }
}

function setErrors(errorElement, code){
    if (code){
        $(errorElement).html(code)
        $(errorElement).removeClass()
        $(errorElement).addClass("text-danger")
    }
    else {
        $(errorElement).html("No Error")
        $(errorElement).removeClass()
        $(errorElement).addClass("text-success")
    }
}