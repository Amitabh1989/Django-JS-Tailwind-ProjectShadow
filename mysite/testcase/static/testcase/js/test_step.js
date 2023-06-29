/* global console */
"use strict";
// Check if localStorage variable exists.
// If no, create it...else use it.
// Take the length of the dictionary and keep adding step number to it.
// When a step is deleted or inserted, handle that accordingly.

function getTestStep(log=true) {
    var testSteps = localStorage.getItem('testSteps');
    if (testSteps === null) {
        testSteps = {};
    } else {
        // testSteps = JSON.parse(JSON.stringify(testSteps));
        testSteps = JSON.parse(testSteps);
    }
    if (log) {
        console.log("Test Case dictionary : ");
        console.log(testSteps);
    }
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
        var stepString = `
            <div class="border border-grey-600 mr-4 ml-4 mb-1 rounded-sm">
                <div class="flex items-center">
                    <span>Test Step ${stepNo}</span>
                    <div class="w-1/10 edit-step bg-grey-400 p-1 text-sm text-black text-center font-bold m-2">
                        <input type="button" value="Edit" data-test-step="${stepNo}">
                    </div>
                </div>
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

        // Check if the value being submitted is edited or new. And act accordingly
        const submitType = document.getElementById("submit-step");
        if (submitType.value === 'Save Edited Step') {
            console.log("Saving Edited Step");
            const stepNo = parseInt(document.querySelector(".module-name").innerHTML.split(" ")[2]);
            console.log("Step number is : " + stepNo);
            testSteps.moduleForm[stepNo-1] = formValues;
        } else {
        // Append the form values to the 'formValues' array
            testSteps.moduleForm.push(formValues);
        }

        // Send the test step list to display submitted steps in Test Step area
        displayTestSteps();

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testSteps));
        console.log("Updated cart : ");
        console.log(testSteps);
    });


    document.addEventListener('click', function(event) {
        console.log("Edit button clicked");
        if (event.target.matches(".edit-step input[type='button']")) {
            // Get the step number from click
            let testStepId = event.target.getAttribute('data-test-step');
            console.log("Test Step " + testStepId + " selected to be edited");


            // Go to Index in the localStorage testStepList and get the module name
            // let tcDict = JSON.stringify(getTestStep(false));
            let tcDict = getTestStep(false);
            console.log("TcDict : " + tcDict);
            let moduleDict = tcDict["moduleForm"];
            let stepDict = moduleDict[testStepId-1];
            stepDict["stepNo"] = testStepId;
            console.log("StepDict : " + JSON.stringify(stepDict));

            // Compose an Ajax request and fetch the values from Database
            ajaxRequest(JSON.stringify(stepDict));
            // Populate the page with the request
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submitToDB() {
    var xhttp = new XMLHttpRequest();
    // Below has been commented as we can either use the submit variable 
    // directly instead of using the jquery below iwth # or like this. as below.
    // submit = document.getElementById("submit-to-db");
    console.log("Got the Submit button");

    // Get the Values from testStepCart
    var testSteps = getTestStep();
    // console.log("Test Steps are : " + JSON.stringify(testSteps));

    // // make a AJAX request
    $.ajax({
        url: '/testcase/success/',
        method: "POST",
        data: JSON.stringify(testSteps),
        success: function(response) {
            // Can add additional data handling here upon success
            console.log(response.resp);
        },
        error: function(xhr, status, error) {
            console.log("Error  : " + error);
            console.log("Status : " + status);
            console.log("XHR    : " + xhr);
        },
        dataType: 'json',
        beforeSend: function(xhr) {
            console.log("Data is ready to be send : " + xhr);
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
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

function edit() {

}


function ajaxRequest(stepDict) {
    console.log("Creating AJAX request now");
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log("Status   : " + xhttp.status);
        // console.log("Response : " + xhttp.responseText);
        if (xhttp.status >= 200 && xhttp.status < 300) {
            const context_data = JSON.parse(xhttp.responseText);
            const formToLoad = context_data.form;

            console.log("Successfull : ");
            document.getElementById('config-form').form = formToLoad;
            document.getElementById('submit-step').value = 'Save Edited Step';
            console.log("FInding the Edit the step DOM : " + document.querySelector('.module-name').innerHTML);
            const stepDictParsed = JSON.parse(stepDict);
            document.querySelector('.module-name').innerHTML = `Edit Step ${stepDictParsed["stepNo"]}`;
            console.log("Step Dict : " + stepDict);

            // for (const fieldName in JSON.parse(stepDict)) {
            for (const fieldName in stepDictParsed) {
                console.log("Field Name : " + fieldName);
                const fieldValue = stepDictParsed[fieldName];
                const fieldElement = document.getElementById("id_" + fieldName);
                console.log("FiledValue : " + fieldValue + "  FiledElement : " + fieldElement);

                if (fieldElement) {
                    fieldElement.value = fieldValue;
                    }
                }

            } else {
                console.log("Status from fail  : " + xhttp.status);
            }
    }
    // Modify the URL by appending query parameters
    const url = '/myapp/?is_ajax=True&send_data=True';
    xhttp.open('GET', url);
    xhttp.send();
}
