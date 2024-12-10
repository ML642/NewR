let count = function()
{
  let counter = 0
    return function()
    {
       return counter++ 
    }
}




let counter = count()
console.log(counter())
console.log(counter())
console.log(counter())
console.log(counter())
