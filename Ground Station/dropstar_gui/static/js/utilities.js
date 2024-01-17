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
        $(motor).html(`Error  \t\t (${speed})`)
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

function setLOStatus(lo, status){
    if (status == false){
        $(lo).html("OFF")
        $(lo).removeClass()
        $(lo).addClass("text-danger")
    }
    else if (status == true){
        $(lo).html("ON")
        $(lo).removeClass()
        $(lo).addClass("text-success")
    }
    else {
        $(lo).html(`Error  \t\t (${status})`)
        $(lo).removeClass()
        $(lo).addClass("text-warning")
        $(lo).addClass("text-dark")
    }
}

function setSOEStatus(soe, status){
    if (status == false){
        $(soe).html("OFF")
        $(soe).removeClass()
        $(soe).addClass("text-danger")
    }
    else if (status == true){
        $(soe).html("ON")
        $(soe).removeClass()
        $(soe).addClass("text-success")
    }
    else {
        $(soe).html(`Error  \t\t (${status})`)
        $(soe).removeClass()
        $(soe).addClass("text-warning")
        $(soe).addClass("text-dark")
    }
}

function setSODSStatus(sods, status){
    if (status == false){
        $(sods).html("OFF")
        $(sods).removeClass()
        $(sods).addClass("text-danger")
    }
    else if (status == true){
        $(sods).html("ON")
        $(sods).removeClass()
        $(sods).addClass("text-success")
    }
    else {
        $(sods).html(`Error  \t\t (${status})`)
        $(sods).removeClass()
        $(sods).addClass("text-warning")
        $(sods).addClass("text-dark")
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