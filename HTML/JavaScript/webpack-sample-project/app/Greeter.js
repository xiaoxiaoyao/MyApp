// Greeter.js
var config = require('./config.json');

module.exports = function() {
    var greet = document.createElement('div');
    greet.textContent = "// Greeter.js    Hi there and greetings!";
    var newTextFromJson = document.createElement('p');
    newTextFromJson=document.createTextNode(config.greetText);
    greet.appendChild(newTextFromJson);
    return greet;
  };