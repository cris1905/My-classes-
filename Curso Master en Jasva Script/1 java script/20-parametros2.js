'use strict'


//parametros REST Y SPREAD

function listadofrutas(fruit1, fruit2, ...resto_de_frutas){
	console.log("Fruta 1: ",fruit1);
	console.log("fruta 2: ",fruit2);
	console.log(resto_de_frutas);
}

listadofrutas("Naranja", "manzana", "sandía", "pera", "uva");

var frutas = ["naranjo", "manzana"];
listadofrutas(...frutas, "sandía", "pera", "uva");