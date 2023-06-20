// Check if localStorage variable exists.
// If no, create it...else use it.
// Take the length of the dictionary and keep adding step number to it.
// When a step is deleted or inserted, handle that accordingly.




// function getTestStep() {
//     var testSteps = localStorage.getItem('testSteps') || {};
//     // if (testSteps === null) {
//     //     testSteps = {};
//     // } else {
//     //     testSteps = JSON.parse(testSteps);
//     // }
//     console.log("Test Case dictionary : " + testSteps);
//     // localStorage.setItem('testSteps', JSON.stringify(cart));
// };

// getTestStep();

$(document).ready(function() {
    $(document).on('click', '.submit-step', function() {
        console.log("The submit-step button is clicked now");

        // Retrieve the form and its values
        var form = $(this).closest('form');
        var formValues = {};
        form.serializeArray().forEach(function(field) {
            formValues[field.name] = field.value;
        });
        console.log("Form Values : " + formValues);
        // Retrieve the testSteps from localStorage
        var testSteps = JSON.parse(localStorage.getItem('testSteps')) || {};

        // Check if 'formValues' property exists
        if (!testSteps.hasOwnProperty('moduleForm')) {
            testSteps.moduleForm = [];
        };

        // Append the form values to the 'formValues' array
        testSteps.moduleForm.push(formValues);

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testSteps));

        console.log("Updated cart : ", testSteps);
    });
});