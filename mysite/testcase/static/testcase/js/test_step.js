/* global console */
"use strict";
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

function displayTestSteps() {
    var testStepsAll = getTestStep();
    var testSteps = testStepsAll.moduleForm;
    var testStepCart = document.getElementsByClassName("tc-cart");
    console.log("TC cart fetched");
    testStepCart[0].innerHTML = "";
    let step = null;
    let stepNo = null;
    for (let i = 0;  i < testSteps.length; i++) {
        step = testSteps[i];
        stepNo = i + 1;
        var stepString = `<div class="border border-grey-600 mr-4 ml-4 mb-1 rounded-sm">
            Test Step ${stepNo}
        </div>`;

        testStepCart[0].innerHTML += stepString;
    }
}

// Send the test step list to display submitted steps in Test Step area
displayTestSteps();

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

        // Send the test step list to display submitted steps in Test Step area
        displayTestSteps();

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testSteps));
        console.log("Updated cart : ");
        console.log(testSteps);
    });
});

function submitToDB() {
    var xhttp = new XMLHttpRequest();
    // Below has been commented as we can either use the submit variable 
    // directly instead of using the jquery below iwth # or like this. as below.
    // submit = document.getElementById("submit-to-db");
    console.log("Got the Submit button");

    // Get the Values from testStepCart
    var testSteps = getTestStep();
    console.log("Test Steps are : " + JSON.stringify(testSteps));

    // make a AJAX request
    $.ajax({
        url: '/testcase/success/',
        method: "POST",
        data: JSON.stringify(testSteps),
        success: function(response) {
            // Can add additional data handling here upon success
            console.log(response);
        },
        error: function(xhr, status, error) {
            console.log("Error  : " + error);
            console.log("Status : " + status);
            console.log("XHR    : " + xhr);
        },
        dataType: 'json',
        beforeSend: function(xhr) {
            console.log("Data is ready to be send : " + xhr);
            xhr.setRequestHeader("X-CSRFToken", JSON.stringify(testSteps)[0]["csrfmiddlewaretoken"]);
        },
        complete: function() {
            console.log("Request Complete");
        },
        timeout: 5000
    });

    // Log to console that the data has been submitted
    console.log("Data has been submitted")
}

$("#submit-to-db").click(submitToDB);