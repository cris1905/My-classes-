'use strict'

//operadores
var num1 = 7;
var num2 = 12;
var operacion = num1 * num2;

alert("Es resultado de la operación es: "+operacion);

//tipos de datos
var numero_entero = 44; //int
var cadena_texto = "hola"; //str
var verdadero_o_falso = true; //buleano

var numero_falso = "33";

// number();

// console.log(ParseInt(numero_falso)+7); //para convertirlo en entero
// console.log(ParseFloat(numero_falso)+7); //para convertirlo en decimal
console.log(String(numero_entero)+4); //para coveretilo en string

// para detectar el tipo de variables
console.log(typeof numero_entero);
console.log(typeof cadena_texto);
console.log(typeof verdadero_o_falso);
console.log(typeof numero_falso);