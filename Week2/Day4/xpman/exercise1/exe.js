// 🌟 Exercise 1 : Information

// Instructions

// Part I : function with no parameters

// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.


// Part II : function with three parameters

// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")


function infoAboutMe(){

    console.log("My name is Sebastian, I am trying to be become a developer.");
}

infoAboutMe()

function infoAboutPerson(personName, personAge, personFavoriteColor){

    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite ${personFavoriteColor}`);
}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")