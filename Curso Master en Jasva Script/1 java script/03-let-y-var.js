'user strict'

// pruebas con let y var
var numero = 30;

if(true){
	var numero = 50;
	console.log(numero); // valor 50
}

console.log(numero); //valor 50

// prueba con let 
var texto = "Curso JS victorrrobleweb.es";
console.log(texto); // valor js

if(true){
	let texto = "curso laravell 5 victorrrobleweb.es";
	console.log(texto); //valor laravel 5
}

console.log(texto); //valor js