
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
"invertColor": function () {
    for (var i = 0; i < fields.length; i++) {
    var color = fields[i].style.backgroundColor;
    if(color == "rgb(255, 255, 255)") {
        fields[i].style.backgroundColor = "#000";
    }
    else {
        fields[i].style.backgroundColor = "#fff";
    }
    }   
}
}
