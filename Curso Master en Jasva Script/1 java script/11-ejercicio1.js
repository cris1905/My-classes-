'use strict'

//programa que pida dos números y que nos diga cual es el mayor, el menor y si son iguales
// plus: si los numeros no son un numero o son menores o iguales a cero, nos los vuelva a pedir

var num1 = parseInt(prompt('introduce el primer número',0));
var num2 = parseInt(prompt('introduce el segundo número',0));

while(num1 <= 0 || num2 <= 0 || isNaN(num1,num2)){
	num1 = parseInt(prompt('introduce el primer número',0));
    num2 = parseInt(prompt('introduce el segundo número',0));
    alert ("INGRESE EL DATO CORRECTO");
    // break;

}
if (num1 == num2){
	alert("los números son iguales");
}else if (num1 > num2){
	alert("El numero mayor es:" + num1);
	alert("El numero menor es:" + num2);

}else if (num2 > num1){
	alert("El numero mayor es:" + num2);
	alert("El numero menor es:" + num1);

}else{
	alert("introduce el número correcto");
}