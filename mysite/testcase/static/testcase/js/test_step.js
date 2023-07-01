/* global console */
"use strict";

/** 
 * Gets the localStorage content and returns the JSON object
 * @param {boolean} [log=true] - If we want to log the content of the cart
*/
function getTestStep(log=true) {
    var testSteps = localStorage.getItem('testSteps');
    if (testSteps === null) {
        testSteps = {};
    } else {
        testSteps = JSON.parse(testSteps);
    }
    if (log) {
        console.log("Test Case dictionary : ");
        console.log(testSteps);
    }
    return testSteps;
}

/**
 * Takes the content of the cart and displays it in test step pane
 */
function displayTestSteps() {
    var testStepsAll = getTestStep();
    var testSteps = testStepsAll.moduleForm;
    var testStepCart = document.getElementsByClassName("tc-cart");
    console.log("TC cart fetched");
    testStepCart[0].innerHTML = "";
    let step = null;
    let stepNo = null;
    var stepString = `<div class="mr-1 ml-1 mb-1 rounded-sm">
                        <div class="flex flex-col rounded-sm">`;
    for (let i = 0;  i < testSteps.length; i++) {
        step = testSteps[i];
        stepNo = i + 1;
        stepString += `
                <div class="flex flex-row hover:scale-105 hover:bg-sky-100">
                    <div class="flex-initial w-96 text-blue-400 text-left text-sm font-bold ml-auto"><span>Test Step ${stepNo}</span></div>
                    <div class="flex w-32">
                        <div class="edit-step text-yellow-500 px-1 text-xs text-right font-bold cursor-pointer mr-1">
                            <input type="button" value="Edit" edit-test-step="${stepNo}">
                        </div>
                        <div class="delete-step text-yellow-500 px-1 text-xs text-right font-bold cursor-pointer mr-1">
                            <input type="button" value="Delete" delete-test-step="${stepNo}">
                        </div>
                    </div>
                </div>`;
    }
    stepString += `</div> </div>`;
    testStepCart[0].innerHTML += stepString;
}

// Send the test step list to display submitted steps in Test Step area
displayTestSteps();


/**
 * Add an ajz here, as soon as the step is submitted, run a query and get the PK of the 
 * Step being submitted
 */
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

        // Send Ajax request to get the PK of the step. If step is not found
        // in the DB, its a new step. never tried
        getTestStepStats(formValues);

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testSteps));
        console.log("Updated cart : ");
        console.log(testSteps);
    });


    document.addEventListener('click', function(event) {
        console.log("Edit button clicked");
        if (event.target.matches(".edit-step input[type='button']")) {
            // Get the step number from click
            let testStepId = event.target.getAttribute('edit-test-step');
            console.log("Test Step " + testStepId + " selected to be edited");


            // Go to Index in the localStorage testStepList and get the module name
            // let tcDict = JSON.stringify(getTestStep(false));
            let tcDict = getTestStep(false);
            console.log("TcDict : " + tcDict);
            let moduleDict = tcDict["moduleForm"];
            let stepDict = moduleDict[testStepId-1];
            stepDict["stepNo"] = testStepId;
            console.log("StepDict : " + JSON.stringify(stepDict));

            // Compose an Ajax request and fetch the module form - from Database
            ajaxRequest(JSON.stringify(stepDict));
            // Populate the page with the request
        }
    });
});

function getTestStepStats(formValues) {
    delete formValues["csrfmiddlewaretoken"];
    let queryString = "";
    Object.keys(formValues).forEach(function(key) {
        queryString += key + "=" + formValues[key] + '&';
    });
    console.log("Fetching step data : " + queryString);
    // const url = '/testcase/teststep_stats/?' + new URLSearchParams(queryString);
    const url = '/testcase/teststep_stats/?' + queryString;
    console.log('Get Request : ' + url)
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                console.log("Response received : " + JSON.stringify(xhr.responseText));
            }
        }
    }
    xhr.send();
}

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
            console.log("Test Case is saved buddy : " + response.resp);
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

/**
 * Sends AJAX request to the backend and fetches the form for the module to be edited.
*/
 function ajaxRequest(stepDict) {
    console.log("Creating AJAX request now");
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        editStepFormHandler(xhttp, stepDict);
        autoReloadDetailView();
    };
    // Modify the URL by appending query parameters
    const url = '/myapp/?is_ajax=True&send_data=True';
    xhttp.open('GET', url);
    xhttp.send();
}


/**
 * Handles the ajaxRequest onload functionality
 * @param {*} xhttp : The XMLHttpRequest object
 * @param {*} stepDict : The step dict of the selected step
 */
function editStepFormHandler(xhttp, stepDict) {
    console.log("Status   : " + xhttp.status);
    // console.log("Response : " + xhttp.responseText);
    if (xhttp.status >= 200 && xhttp.status < 300) {
        const context_data = JSON.parse(xhttp.responseText);
        const formToLoad = context_data.form;

        console.log("Successfull : ");
        document.getElementById('config-form').form = formToLoad;
        document.getElementById('submit-step').value = 'Save Edited Step';
        console.log("Finding the Edit the step DOM : " + document.querySelector('.module-name').innerHTML);
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

// Once the test step is submitted, then call the analytics on the test step
// Also, refresh the other analytics

function autoReloadDetailView(callback = () => {}) {
    const xhr = new XMLHttpRequest();
    console.log("Inside the autoreload");
    xhr.open('GET', '/testcase/teststep_detail/38/', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const jsonResponse = JSON.parse(xhr.responseText);
                document.getElementById('teststep-container').innerHTML = "JS return " + xhr.responseText + "====";
                callback(jsonResponse);
            } else {
                console.log('Status : ' + xhr.status);
            }
        }
    }
    xhr.send()
}

autoReloadDetailView();
document.addEventListener('DOMContentLoaded', function() {
    autoReloadDetailView(function(jsonResponse) {
        testStepDetails(jsonResponse);
    });
});


/**
 * Display the statos for the test step submitted
 */
function testStepDetails(jsonResponse) {
    console.log("Response received : " + jsonResponse)
    const ctx = document.getElementById('myChart');
    const testCases = jsonResponse.test_cases;
    console.log("Test Case : " + JSON.stringify(testCases));
    const cqIDSet = new Set();
    const dateSet = new Set();
    const dataValues = testCases.map(testCase => {
        console.log("Element: " + JSON.stringify(testCase.cqid));
        cqIDSet.add(testCase.cqid);
        dateSet.add(new Date(testCase.updated_on).toLocaleDateString());
        return 1; // or any other value you want to assign to each test case
    });
    console.log("CQIDSET : " + [...cqIDSet]);
    console.log("DATESET : " + [...dateSet]);
    console.log("DATEVALUES : " + [...dataValues]);
    new Chart(ctx, {
        type: 'bar',
        data: {
        labels: [...dateSet],
        datasets: [{
            label: '# of Test Cases',
            data: dataValues,
            borderWidth: 1
        }]
        },
        options: {
        scales: {
            y: {
            beginAtZero: true
            }
        }
        }
    });
}