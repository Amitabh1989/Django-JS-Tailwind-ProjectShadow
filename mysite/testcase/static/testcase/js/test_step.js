/* global console */
// Check if localStorage variable exists.
// If no, create it...else use it.
// Take the length of the dictionary and keep adding step number to it.
// When a step is deleted or inserted, handle that accordingly.

function getTestStep() {
    var testSteps = localStorage.getItem('testSteps');
    if (testSteps === null) {
        testSteps = {};
    } else {
        // testSteps = JSON.parse(JSON.stringify(testSteps));
        testSteps = JSON.parse(testSteps);
    }
    console.log("Test Case dictionary : ");
    console.log(testSteps);
    return testSteps;
}


$(document).ready(function () {
    $(document).on('click', '.submit-step', function () {

        console.log("The submit-step button is clicked now");

        // Retrieve the form and its values
        var form = $(this).closest('form');

        // Stop the form from submitting to the Database
        form.on('submit', function (e) {
            e.preventDefault();
            console.log("Form submission behaviour altered");
        });

        var formValues = {};
        form.serializeArray().forEach(function (field) {
            formValues[field.name] = field.value;
        });
        console.log("Form Values : " + JSON.stringify(formValues));

        // Retrieve the testSteps from localStorage
        var testSteps = getTestStep();
        console.log("Before Update, cart : ", testSteps);

        // Check if 'formValues' property exists
        if (!testSteps.hasOwnProperty('moduleForm')) {
            testSteps.moduleForm = [];
        }

        // Append the form values to the 'formValues' array
        testSteps.moduleForm.push(formValues);

        // Update the 'testSteps' in localStorage
        // localStorage.setItem('testSteps', JSON.stringify(testSteps));
        localStorage.setItem('testSteps', JSON.stringify(testSteps));

        console.log("Updated cart : ");
        console.log(testSteps);
    });
});
