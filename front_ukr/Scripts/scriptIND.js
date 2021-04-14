let pageSystem = "ky";
let URL = "http://localhost:8000/translate"

let title = document.getElementById("headerText").innerText;
let helpText = document.getElementById("helpInfoText").innerText;
let radioButtom = document.getElementsByName("systemToLabel");
let about = document.getElementById("about").innerText;
let developer = document.getElementById("developer").innerText;
let copyLink = document.getElementById("copyLink").innerText;

let textPage = radioButtom[0].innerText + " | " + radioButtom[1].innerText + " | " + radioButtom[2].innerText + " | " + title + " | " + helpText + " | " +  about + " | " + developer + " | " + copyLink;

function changePageSystem(elem) {
    console.log(elem.value);
    state = 0; 
    pageSystem = elem.value;
    if (pageSystem == "ky") {
        setSystemPage(textPage);
    } else {
        let data = {"fromSystem": "ky", "toSystem": pageSystem, "text": textPage}
        postData(URL, data)
            .then((data) => {
            setSystemPage(data["message"]);
        });
    }
}

function setSystemPage(text) {
    arrayOfValues = text.split(" | ");
    

    let radioButtom = document.getElementsByName("systemToLabel");
    console.log(radioButtom);
    for (i = 0; i < 3; i++) {
        radioButtom[i].innerText = arrayOfValues[i];
    }

    radioButtom = document.getElementsByName("systemFromLabel");
    radioButtom[0].innerText = arrayOfValues[0];
    radioButtom[1].innerText = arrayOfValues[1];

    document.getElementById("headerText").innerText = arrayOfValues[3];
    document.getElementById("helpInfoText").innerText = arrayOfValues[4];
    document.getElementById("about").innerText = arrayOfValues[5];
    document.getElementById("developer").innerText = arrayOfValues[6];
    document.getElementById("copyLink").innerText = arrayOfValues[7];
}

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
      method: 'POST',
      mode: 'cors',
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json'
      },
      redirect: 'follow',
      referrerPolicy: 'no-referrer',
      body: JSON.stringify(data)
    });
    return await response.json();
  }
  