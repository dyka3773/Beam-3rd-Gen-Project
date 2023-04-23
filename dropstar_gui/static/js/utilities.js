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
        // $(motor).addClass("text-primary")
    }
    else {
        $(motor).html(`Error  \t\t (${speed})`)
        $(motor).css("bg-color", "black")
        $(motor).css("color", "white")
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
        $(soundCard).css("bg-color", "black")
        $(soundCard).css("color", "white")
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
        $(camera).css("bg-color", "black")
        $(camera).css("color", "white")
    }
}