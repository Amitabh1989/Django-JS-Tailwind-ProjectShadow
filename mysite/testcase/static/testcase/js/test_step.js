// Check if localStorage variable exists.
// If no, create it...else use it.
// Take the length of the dictionary and keep adding step number to it.
// When a step is deleted or inserted, handle that accordingly.




function getTestStep() {
    var testSteps;
    if (localStorage.getItem('cart') === null) {
        testSteps = {};
    } else {
        testSteps = JSON.parse(localStorage.getItem('cart'));
    };
    console.log("Test Case dictionary : " + JSON.stringify(testSteps));
};

getTestStep();


/* TO STORE A JSON IN CART
var cart = {
  test: {
    name: "amitabh"
  }
};

localStorage.setItem("cart", JSON.stringify(cart));
*/

var addToCartButton = document.querySelectorAll('.')


/