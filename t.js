"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Element = document.createElement("button");
document.body.childNodes[0].append(Element);
var button = document.body.childNodes[0];
if (button) {
    var flag_1 = true;
    button.onclick = function (event) {
        if (flag_1) {
            button.style.backgroundColor = "yellow";
            flag_1 = false;
        }
        else {
            button.style.backgroundColor = "blue";
            flag_1 = true;
        }
    };
}
