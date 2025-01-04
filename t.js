"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var obj = {
    age: 44,
    workExp: 23,
    name: "Susan",
    MyMethod: function () { return this.age - this.workExp - 18; }
};
obj.age = 55;
console.log(obj.MyMethod());
var Myname;
(function (Myname) {
    Myname["first"] = "string";
    Myname["second"] = "smt else";
    Myname["third"] = "forth";
    Myname["fourth"] = "new line";
})(Myname || (Myname = {}));
var newvariable = Myname.first;
var oldvariable = Myname.second;
var Persona = {
    name: "Jusef",
    age: 32,
    work: "kol",
    id: [1, 2, 3, 1, 34, 4]
};
var id = Math.floor(Math.random() * 1000);
var Newman = {
    age: 15,
    position: "junior",
    salary: 9000,
};
var ourunion;
if (typeof ourunion == "string") {
    console.log(ourunion.toUpperCase());
}
