//Content
function loadContent(name, ID) {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', `../content/${name}.html`, true);

    xhr.onload = function () {

        if (xhr.status >= 200 && xhr.status < 300) {

            document.getElementById(ID).innerHTML = xhr.responseText;

        } else {

            console.error('Fehler beim Laden der Datei:', xhr.statusText);

        }

    };

    xhr.onerror = function () {

        console.error('Netzwerkfehler');

    };

    xhr.send();

}

//Galerie

function loadImg(num) {
    const modal = document.getElementById('img-modal');
  
    modal.innerHTML = 
    `<div class="modal-dialog modal-xl modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-body" id="img-modal">
              <img class="w-100" src="../static/img/${num}-min.jpg" alt="Ladefehler">
            </div>
          </div>
        </div>`
  }