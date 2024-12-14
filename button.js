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
let newe = 1234 

class Creature { 
   constructor(age,gender)
   {
  this.age = age 
  
  this.gender = gender 
   }
   
   get Getage (){ 
    return this.age 
}
   set Setage(number){
this.age = number 
}
   #method(){
    console.log(" checking in ")
   }
   static Sort(){console.log("sorted")}
}
class worker extends Creature {
    constructor(age,gender,work_experience,position,salary ){
        super (age,gender)
        this.work_experience = work_experience
        this.position = position
        this.salary = salary
    }


}
let elemen2t = document.createElement("div")
let newelement = document.createElement("p")

let some = 0 
let sum = 1999 
let age =12