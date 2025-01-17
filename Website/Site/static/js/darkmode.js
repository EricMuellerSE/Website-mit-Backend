//Darkmode
let darkmode = localStorage.getItem('darkmode');

function checkDarkmode(){
    if (darkmode === "active") enabledarkmode();
}

function enabledarkmode() {
    document.body.classList.add('darkmode');
    localStorage.setItem('darkmode', 'active');
}

function disabledarkmode() {
    document.body.classList.remove('darkmode');
    localStorage.setItem('darkmode', null);
}

// Überprüfen, ob der Darkmode aktiv ist und anwenden
darkmode = localStorage.getItem('darkmode');
if (darkmode === "active") enabledarkmode();

function modeSwitch() {
    darkmode = localStorage.getItem('darkmode');
    darkmode !== "active" ? enabledarkmode() : disabledarkmode();
}