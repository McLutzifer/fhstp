
let field;
const renderChess = (startColor) => {
    let widthAndHeight = 60;
    for (let j = 0; j < 8; j++) {
        for (let i = 0; i < 8; i++) {
            field = document.createElement("div");
            field.style.position = "absolute";
            field.style.width = widthAndHeight + "px";
            field.style.height = widthAndHeight + "px";
            field.style.left = i * widthAndHeight + "px";
            field.style.top = j * widthAndHeight + "px";
            let color = startColor;
            if((i+j) % 2 === 0) {
                if (startColor == "#000")
                    color = "#fff"
                else
                    color = "#000"
            }
            field.style.background = color;
            field.id = i + j * 8;
        document.getElementById("chess").appendChild(row);
    }

}


const invertieren = () => {
    for (var i = 0; i < 8 * 8; i++) {
        var element = document.getElementById(i);
        var color = element.style.backgroundColor;
        if (color == "rgb(255, 255, 255") {
            element.style.backgroundColor = "rgb(0, 0, 0)";
        }
        else {
            element.style.backgroundColor = "#fff";
        }
    }
}