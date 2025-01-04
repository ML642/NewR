    export {}
    
    let obj : {age ?: number, workExp ?: number , name ?: string , MyMethod : ()=>number} =  {
        age : 44 , 
        workExp : 23 , 
        name : "Susan",
        MyMethod : function()  {return this.age-this.workExp-18}

    }
    
    obj.age = 55

    console.log(obj.MyMethod())

    enum Myname {
    first = "string",
    second = "smt else",
    third ="forth",
    fourth="new line"
    }
    let newvariable = Myname.first 

    let oldvariable = Myname.second 

    type Numeric = number 

    type Person  = {
        name : string  , 
        age : number ,
        work : string ,
        id : number[]
    }
    let Persona : Person = {
        name : "Jusef" ,
        age: 32 ,
        work :"kol" , 
        id : [1,2,3,1,34,4]  
    } 

    let id : Numeric = Math.floor(Math.random()*1000)


  interface Human {
     stamina ?: number , 
     speed ?: number ,
     smtElse ?: string 
  }

  interface Worker extends Human 
  {
    age ?: number , 
    position ?: string , 
    salary ?: number 
  }

  let Newman : Worker = {
    age: 15 , 
    position : "junior",
    salary : 9000 ,
    
}

let ourunion : string | number    

 if(typeof ourunion == "string"){
    console.log(ourunion.toUpperCase())
 }
