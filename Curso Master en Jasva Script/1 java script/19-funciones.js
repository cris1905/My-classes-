'use strict'

// funciones
// una función es una agrupación reutilizable de un conjunto de instruciones

function calculadora(num1, num2, mostrar = false){

	//conjunto de instruciones a ejecurtar 
	// console.log("Hola soy la calculadora");
	// console.log("si soy yo");
	if(mostrar == false){
		console.log("suma: "+(num1+num2));
		console.log("resta: "+(num1-num2));
		console.log("multiplicación: "+(num1*num2));
		console.log("división: "+(num1/num2));
		console.log("****************************");

	}else{
		document.write("suma: "+(num1+num2)+"<br/>");
	    document.write("resta: "+(num1-num2)+"<br/>");
		document.write("multiplicación: "+(num1*num2)+"<br/>");
		document.write("división: "+(num1/num2)+"<br/>");
		document.write("****************************");
	}

	// return "hola soy yo";	
}

// llamar a la función 
// for(var i = 1; i <= 10; i++){
// 	console.log(i);
// 	calculadora(i, 8);
// }
calculadora(1, 4);
calculadora(2, 5, true);