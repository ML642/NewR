let element = document.getElementsByTagName("p")[0]

let button = document.createElement("button")

element.append(button)
let flag = 0
button.onclick = function (){
    if(flag == 0 ){document.body.style.background = "red"; flag = 1}
    if(flag == 1 ){document.body.style.background = "blue" ; flag = 0 } 

}