let fields = [];
function drawChessboard (startColor) {
    let widthAndHeight = 60;
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            let field = document.createElement("div");
            field.style.position = "absolute";
            field.style.width = widthAndHeight + "px";
            field.style.height = widthAndHeight + "px";
            field.style.left = i * widthAndHeight + "px";
            field.style.top = j * widthAndHeight + "px";
            let color = startColor;
            if((i+j) % 2 === 0) {
                if (startColor == "#000")
                    color = "#fff";
                else
                    color = "#000";
            }
            field.style.backgroundColor = color;
            field.id = i + j * 8;
            fields.push(field);
            document.getElementById("chess").appendChild(field);
        }
 
    }
}

function invertColor() {
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
