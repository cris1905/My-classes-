'use strict'

// tabla de multiplicar de un numero introducido por pantalla

var numero = parseInt(prompt('de que numero quieres la tabla?', 1));
document.write("<h1>Tabla del "+numero+"</br>");
for(var i = 1; i<= 10; i++){
	document.write(i+" x "+numero+" = "+(i*numero)+"</br>"); //para mostrarlo directamente en la web
}

// todas la tablas 

// for (var c = 1; c<= 12; c++){
// 	document.write("<h1>Tabla del "+c+"</br>");
// for(var i = 1; i<= 10; i++){
// 	document.write(i+" x "+c+" = "+(i*c)+"</br>"); //para mostrarlo directamente en la web
// }



// }