let element = document.getElementsByTagName("p")[0]

let button = document.createElement("button")

button.style.height = "100px"
button.style.width = "210px"
element.append(button)
let flag = 0   
button.onclick = function (){
    
    if(flag == 0 ){document.body.style.background = "yellow"; flag = 1 ; return }
   
    if(flag == 1 ){document.body.style.background = "blue" ; flag = 0  ; return } 
    console.log(flag)
    
}
const nwConts = 123  ;
