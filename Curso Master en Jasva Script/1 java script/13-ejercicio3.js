'use strict'

/*
hacer un programa que muestre todos los numeros entre dos numeros introducidos por el usuario
*/

var num1 = parseInt(prompt("introduce el primer numero", 0));
var num2 = parseInt(prompt("introduce el segundo numero", 0));

document.write("<h1>Del "+num1+" a "+num2+" estan estos numeros:</h1>")
for(var i = num1; i <= num2; i++){
	document.write(i+"<br/>");

}