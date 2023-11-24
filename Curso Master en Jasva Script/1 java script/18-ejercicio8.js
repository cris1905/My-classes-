'use strict'

// Calculadora:
// pida dos numeros por pantallas
// -si metemos uno mal que nos los vuelva a pedir
// -en el cuerpo de la pagina, en una alerta y por la consola el resultado de
// sumas, restar,multiplicar y dividir esas dos cifras

var num1 = parseInt(prompt("introduce el primer numero", 0)); //parseInt para convertir  el string en un entero
var num2 = parseInt(prompt("introduce el segundo numero", 0));

while(num1 <= 0 || num2 <= 0 || isNaN(num1,num2)){
	num1 = parseInt(prompt('introduce el primer número',0));
    num2 = parseInt(prompt('introduce el segundo número',0));
    alert ("INGRESE EL DATO CORRECTO");
    // break;

}

var resultado = "La suma es "+(num1+num2)+"</br>"+
                "La resta es "+(num1-num2)+"</br>"+
                "La multiplicación es "+(num1*num2)+"</br>"+
                "La divición es "+(num1/num2)+"</br>"; 

var resultadocmd = "La suma es "+(num1+num2)+"\n"+
                "La resta es "+(num1-num2)+"\n"+
                "La multiplicación es "+(num1*num2)+"\n"+
                "La divición es "+(num1/num2)+"\n";                 

document.write(resultado);
alert(resultadocmd);

