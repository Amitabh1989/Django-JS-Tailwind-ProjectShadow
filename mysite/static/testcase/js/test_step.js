// Check if localStorage variable exists.
// If no, create it...else use it.
// Take the length of the dictionary and keep adding step number to it.
// When a step is deleted or inserted, handle that accordingly.


function getTestStep() {
    if (localStorage.getItem('testSteps') === null) {
        var testSteps = {};
    } else {
        testSteps = JSON.parse(localStorage.getItem('testSteps'));
    };
};

console.log("Test Case dictionary : " + testSteps);