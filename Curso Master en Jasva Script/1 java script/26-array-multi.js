'use strict'

//los array multidimensionales quiere decir que se puede poner un array dentro de otro

var categorias = ['Ación', 'Terror', 'comedia'];
var peliculas = ['La verdad duele', 'La vida es bella', 'Gran Torino' ];

var cine = [categorias, peliculas];

console.log(cine[0][1]); // con esto puedo acceder a las dimensiones de los arrys
console.log(cine[1][2]);

// var elemento = prompt("Introduce tu pelicula");

// while(elemento != "ACABAR"){   //mi metodo con while en la clase aprendida
//     elemento = prompt("Introduce tu pelicula"); 
//     peliculas.push(elemento);
// }

// var elemento = "";

// do{
//     elemento = prompt("Introduce tu pelicula:");
//     peliculas.push(elemento);
// }while(elemento != "ACABAR");

// peliculas.pop(); // EL POP elimina el último array

// peliculas.push("Batman"); 

var indice = peliculas

console.log(peliculas);
