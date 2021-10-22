
const renderChess = () => {
    let widthAndHeight = 60;
    for (let j = 0; j < 8; j++) {
        let row = document.createElement('div');
        row.id = "row" + j;
        for (let i = 0; i < 8; i++) {
            let field = document.createElement("div");
            field.style.position = "absolute";
            field.style.width = widthAndHeight + "px";
            field.style.height = widthAndHeight + "px";
            field.style.left = i * widthAndHeight + "px";
            let color = "#000"
            if((i+j) % 2 === 0) {
                color = "#fff"
            }
            field.style.background = color;
            row.appendChild(field);
        }
        if(j !== 0) {
            row.style.margin = j * widthAndHeight + "px";
        }
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