'use strict'


//condicional if
// si AS es igual a B haz algo

var edad = 74;
var nombre = 'David';

/*
operadores relacionales
mayor = >
menor = <
mayot


*/
if (edad >= 18){
	//es mayor de edad
	console.log(nombre+" tiene "+edad+" años, es mayor de edad");
	if (edad <= 33){
		console.log("Todavia ere milenial");

	}else if(edad >= 70){
		console.log("Ya eres ansiano");
	}else{
		console.log("ya no ere milenial");
	}
}else{
	//es menor de edad
	console.log(nombre+" tiene "+edad+" años, es menor de edad");
}