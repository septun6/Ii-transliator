let socket = io.connect("localhost:8000");
let data = {};
let state = 0;
setYear();
setYearLink();

//let pageSystem = "ky";
let fromSystem = "ky";
let toSystem = "ln";

// let title = document.getElementById("headerText").innerText;
// let helpText = document.getElementById("helpInfoText").innerText;
// let radioButtom = document.getElementsByName("systemToLabel");
// let about = document.getElementById("about").innerText;
// let developer = document.getElementById("developer").innerText;
// let copyLink = document.getElementById("copyLink").innerText;
    
// let textPage = radioButtom[0].innerText + " | " + radioButtom[1].innerText + " | " + radioButtom[2].innerText + " | " + title + " | " + helpText + " | " +  about + " | " + developer + " | " + copyLink;

textarea = document.getElementById("lastText");
textarea.addEventListener('input', autoResize, false);
     
function autoResize() {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
}

function copyFunction() {
    var newText = document.getElementById("newText")
    navigator.clipboard.writeText(newText.innerText)
    .then(() => {
        alert("Текст скопійован");
    })
    .catch(err => {
    console.log('Something went wrong', err);
     });
}

if (window.matchMedia("(min-width: 900px)").matches) {
    window.onload = function() {
        document.getElementById("lastText").focus();
    };
  }

function setYear() {
    let now = new Date();
    document.getElementById("year").innerHTML = now.getFullYear();
}

function setYearLink() {
    let now = new Date();
    let link = "https://uk.wikipedia.org/wiki/";
    document.getElementById("year").href = link + now.getFullYear();
}

function changeToSystem(elem) {
    toSystem = elem.value;
    console.log(toSystem);
    let element = document.getElementById("lastText");
    changeMessage(element);
}

function changeFromSystem(elem) {
    fromSystem = elem.value;
    console.log(fromSystem);
    let element = document.getElementById("lastText");
    changeMessage(element);
}

// function changePageSystem(elem) {
//     console.log(elem.value);
//     state = 0; 
//     pageSystem = elem.value;
//     if (pageSystem == "ky") {
//         setSystemPage(textPage);
//     } else {
//         translate(pageSystem, "ky", textPage);
//     }
// }

function changeMessage(elem) {
    let text = elem.value;
    state = 1
    if (fromSystem != toSystem) {
        translate(toSystem, fromSystem, text)
                } else {
                    showMessage(text);
                }
            };
            
socket.on('translated', text => {
    if (state == 1) {
        showMessage(text);
    } else {
        setSystemPage(text);
    }
});

// function setSystemPage(text) {
//     arrayOfValues = text.split(" | ");
    

//     let radioButtom = document.getElementsByName("systemToLabel");
//     console.log(radioButtom);
//     for (i = 0; i < 3; i++) {
//         radioButtom[i].innerText = arrayOfValues[i];
//     }

//     radioButtom = document.getElementsByName("systemFromLabel");
//     radioButtom[0].innerText = arrayOfValues[0];
//     radioButtom[1].innerText = arrayOfValues[1];

//     document.getElementById("headerText").innerText = arrayOfValues[3];
//     document.getElementById("helpInfoText").innerText = arrayOfValues[4];
//     document.getElementById("about").innerText = arrayOfValues[5];
//     document.getElementById("developer").innerText = arrayOfValues[6];
//     document.getElementById("copyLink").innerText = arrayOfValues[7];
// }
    
function translate(toSystem, fromSystem, text) {
    data["fromSystem"] = fromSystem;
    data["toSystem"] = toSystem;
    data["text"] = text;   
    socket.emit("translate", data);
    return false;
}

function showMessage(message) {
    document.getElementById("newText").innerHTML = message;
}
