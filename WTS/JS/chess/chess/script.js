
var chessBoard =  {
    "fieldCount": 64,
"widthAndHeight": 60,
"fields": [],

"drawChessboard": function() {
        for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
        let field = document.createElement("div");
        field.style.position = "absolute";
        field.style.width = this.widthAndHeight + "px";
        field.style.height = this.widthAndHeight + "px";
        field.style.left = i * this.widthAndHeight + "px";
        field.style.top = j * this.widthAndHeight + "px";
        let color = "#fff";
        if((i+j) % 2 === 0) {
          color = "#000";
        }
        field.style.backgroundColor = color;
        field.id = i + j * 8;
        this.fields.push(field);
        document.getElementById("chess").appendChild(field);
    }
    }
},
"colorField": function (fieldId, color) {
    var element = this.fields[fieldId];
  element.style.backgroundColor = color;

},

"invertColor": function () {
    for (var i = 0; i < this.fields.length; i++) {
    var color = this.fields[i].style.backgroundColor;
    if(color == "rgb(255, 255, 255)") {
        this.fields[i].style.backgroundColor = "#000";
    }
    else {
        this.fields[i].style.backgroundColor = "#fff";
    }
    }   
},

"placeFigures": function () {
        var serverKommunikation = new XMLHttpRequest();
            serverKommunikation.addEventListener("load", function () {
                var jsonObjekt = JSON.parse(this.responseText);
            });
            serverKommunikation.open("GET", "https://atp.fhstp.ac.at/chessDataJSONDemo");
            serverKommunikation.send();
}
}


var buttonElement = document.querySelector("#renderChess");
buttonElement.onclick = function () {
    chessBoard.drawChessboard();
};

buttonElement = document.querySelector("#colorButton");

/*buttonElement.onclick = function () {
    var inputField1 = document.querySelector("#fieldId");
var inputField2 = document.querySelector("#color");
    chessBoard.colorField(inputField1.value, inputField2.value);
};*/
var myCallbackFunction = function () {
    var inputField1 = document.querySelector("#fieldId");
var inputField2 = document.querySelector("#color");
    chessBoard.colorField(inputField1.value, inputField2.value);
};





buttonElement = document.querySelector("#placeFigures");
var myCallbackFunction2 = function () {
    chessBoard.placeFigures();
};

buttonElement.addEventListener("click", myCallbackFunction2);

