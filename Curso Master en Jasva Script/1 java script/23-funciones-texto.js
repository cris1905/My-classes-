'use strict'

// traformación de texto

var numero = 444;
var texto1 = " bienvenido al curso de javascript de victor robles ";
var texto2 = "Es muy buen curso";

//var busqueda = texto1.match("curso");
//var busqueda = texto1.substr(14,5); //para seleccionar lo que tiene el texto = curso
//var busqueda = texto1.charAt(44); // para sacr una letra concreta de un string
// var busqueda = texto1.startsWith("victor");
// var busqueda = texto1.endsWith("victor robles");
//var busqueda = texto1.incluides("victor robles"); //para buscar una palabra exacta
// var busqueda = texto1.replace("javascript", "syfony"); // para reemplazar una palabra
//var busqueda = texto1.slice(16); // para cortar los caracteres 
//var busqueda = texto1.split(" "); // para recortar las palabras y meterlo en un rango
var busqueda = texto1.trim(); // recortar los espación que te los caracteres

console.log(busqueda);