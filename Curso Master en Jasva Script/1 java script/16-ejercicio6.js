'use strict'

/*
Que nos diga si un numero es par i impar
1. ventana prompt
2.si no es valido que nos pida de nuevo
*/

var number = parseInt(prompt('introduce un numero', 0));

while(isNaN(number)){ // mientras que no sea un numero var a estar dando vueltas 
	var number = parseInt(prompt('introduce un numero', 0));

}

if(number % 2 == 0){
	alert("Es un numero par");
}else{
	alert("Es impar");
}