/* this is a javascript file
console.log("Hello Nyah");
alert("Hi HaoNa");
var nameAnswer = prompt("What's your name?");
console.log("Your name is " + nameAnswer);
*/

// 10. 8, 6, 5, 2, 0
for (var i = 10; i>= 0; i -= 2){
  console.log(i);
}

for (var i = 0; i < 3; i++){
  var answer = prompt("What's your name?");
  greetName(answer);
}



function greetName(name){
  console.log("Hi " + name + "!");
}
