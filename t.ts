export {  }
 
let Element = document.createElement("button")   as HTMLElement

(document.body.childNodes[0] as HTMLElement).append ((Element as HTMLElement))


let button : HTMLElement | null   =  document.body.childNodes[0] as HTMLElement

if( button ){
    let  flag : boolean = true  
    button.onclick = function ( event: MouseEvent) : void {

if(flag) {button.style.backgroundColor  = "yellow" ; flag = false}
else {button.style.backgroundColor = "blue" ; flag = true } 
    } 
} 


