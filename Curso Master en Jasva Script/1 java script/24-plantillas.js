'use strict'

// plantilla de texto

var nombre = prompt("INTRODUCE TU NOMBRE")
var apellidos = prompt("INTRODUCE TU APELLIDO")

//var texto = MIi nombre es: "+nombre+" <br/> Mis apellidos son: "apellidos;
var texto = `
    <h1>hola que tal </h1>
    <h3>Mi nombre es: ${nombre}</h3>
    <h3>Mi apellidos son: ${apellidos}</h3>

`;

document.write(texto);    
