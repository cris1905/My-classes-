'use strict'

// switch

var edad = 18;
var imprime = "";

switch(edad){
    case 18: //para comprovar un caso
        imprime ="Acabas de cumplir la mayoria de edad";
    break;
    case 25: //para comprovar un caso
        imprime ="Ya eres un adulto";
    break;
    case 40: //para comprovar un caso
        imprime ="Crisis de los 40";
    break;
    case 75: //para comprovar un caso
        imprime ="Ya eres un anciano";
    break;
    default:
        imprime = "tu edad es neutra";
    break;    

}
        
console.log(imprime);


