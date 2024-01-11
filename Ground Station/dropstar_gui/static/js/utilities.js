function setMotorStatus(motor, speed){
    if (speed == 0){
        $(motor).html(`Stopped \t\t (${speed})`)
        $(motor).removeClass()
        $(motor).addClass("text-danger")
    }
    else if (speed == 255){
        $(motor).html(`Max Speed \t\t (${speed})`)
        $(motor).removeClass()
        $(motor).addClass("text-success")
    }
    else if (speed > 0){
        $(motor).html(`Speed Up \t\t (${speed})`)
        $(motor).removeClass()
        // $(motor).addClass("text-primary") // This is the default color which is blue
    }
    else {
        $(motor).html(`Error  \t\t (${speed})`)
        $(motor).removeClass()
        $(motor).addClass("text-warning")
        $(motor).addClass("text-dark")
    }
}

function setSoundCardStatus(soundCard, status){
    if (status == false){
        $(soundCard).html("OFF")
        $(soundCard).removeClass()
        $(soundCard).addClass("text-danger")
    }
    else if (status == true){
        $(soundCard).html("ON")
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
    if (status == false){
        $(camera).html("OFF")
        $(camera).removeClass()
        $(camera).addClass("text-danger")
    }
    else if (status == true){
        $(camera).html("ON")
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