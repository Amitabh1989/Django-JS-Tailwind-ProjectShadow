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
                    <div class="flex-initial w-96 text-blue-400 text-left text-sm font-bold ml-auto px-5"><span>Test Step ${stepNo}</span></div>
                    <div class="flex w-32">
                        <div class="edit-step text-yellow-500 px-1 text-xs text-right font-bold pr-2">
                            <input type="button" value="Edit" edit-test-step="${stepNo}">
                        </div>
                        <div class="delete-step text-yellow-500 px-1 text-xs text-right font-bold pr-2">
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
            console.log("Form submission behavior altered");
        });

        var formValues = {};
        form.serializeArray().forEach(function (field) {
            formValues[field.name] = field.value;
        });
        console.log("Form Values: " + JSON.stringify(formValues));

        // Retrieve the testSteps from localStorage
        var testSteps = getTestStep();
        console.log("Before Update, cart: ", testSteps);

        // Check if 'formValues' property exists
        if (!testSteps.hasOwnProperty('moduleForm')) {
            testSteps.moduleForm = [];
        }

        // Check if the value being submitted is edited or new. And act accordingly
        const submitType = document.getElementById("submit-step");
        if (submitType.value === 'Save Edited Step') {
            console.log("Saving Edited Step");
            const stepNo = parseInt(document.querySelector(".module-name").innerHTML.split(" ")[2]);
            console.log("Step number is: " + stepNo);
            testSteps.moduleForm[stepNo - 1] = formValues;
        } else {
            // Append the form values to the 'formValues' array
            testSteps.moduleForm.push(formValues);
        }

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testSteps));
        console.log("Updated cart: ");
        console.log(testSteps);

        // Send Ajax request to get the PK of the step. If step is not found
        // in the DB, it's a new step. never tried
        getTestStepStats(formValues);
        console.log("getTestStepStats called ");
        // Send the test step list to display submitted steps in Test Step area
        displayTestSteps();
    });

    $(document).on('click', function (event) {
        console.log("Edit button clicked");
        if ($(event.target).is(".edit-step input[type='button']")) {
            // Get the step number from click
            let testStepId = $(event.target).attr('edit-test-step');
            console.log("Test Step " + testStepId + " selected to be edited");

            // Go to Index in the localStorage testStepList and get the module name
            let tcDict = getTestStep(false);
            console.log("TcDict : " + tcDict);
            let moduleDict = tcDict["moduleForm"];
            let stepDict = moduleDict[testStepId - 1];
            stepDict["stepNo"] = testStepId;
            console.log("StepDict : " + JSON.stringify(stepDict));

            // Compose an Ajax request and fetch the module form - from Database
            ajaxRequest(JSON.stringify(stepDict));
            // Populate the page with the request

        } else if ($(event.target).is(".delete-step input[type='button']")) {
            // Get the step number from click
            let testStepId = $(event.target).attr('delete-test-step');
            console.log("Test Step " + testStepId + " selected to be deleted");

            // Go to Index in the localStorage testStepList and get the module name
            let tcDict = getTestStep(false);
            console.log("TcDict : " + tcDict);
            let moduleDict = tcDict["moduleForm"];
            let stepDict = moduleDict[testStepId - 1];
            console.log("Deleting elements from index: " + (testStepId - 1));
            moduleDict.splice(testStepId - 1);
            localStorage.setItem('testSteps', JSON.stringify(tcDict));
            console.log("Items deleted");
            // Send the test step list to display submitted steps in Test Step area
            displayTestSteps();
        }
    });
});



/**
 * Will use this to create hyperlinks to the test cases that are displayed in the
 * Card. ==> List of test cases with exact step
 * @param {*} formValues 
 */
// function getTestStepStats(formValues, handleTestStepStatsResponse= () => {}) {
// // function getTestStepStats(formValues) {
//     console.log("Inside getTestStepStats : " + formValues);
//     delete formValues["csrfmiddlewaretoken"];
//     let queryString = "";
//     Object.keys(formValues).forEach(function(key) {
//         queryString += key + "=" + formValues[key] + '&';
//     });
//     console.log("Fetching step data : " + queryString);
//     // const url = '/testcase/teststep_stats/?' + new URLSearchParams(queryString);
//     const url = '/testcase/teststep_stats/?' + queryString;
//     console.log('Get Request : ' + url)
//     const xhr = new XMLHttpRequest();
//     xhr.open('GET', url, true);
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === XMLHttpRequest.DONE) {
//             console.log("XHR status if : " + xhr.status);
//             if (xhr.status === 200) {
//                 const response = JSON.parse(xhr.responseText);
//                 console.log("Response received parsed : " + response);
//                 console.log("Response received string : " + JSON.stringify(response));
//                 if (typeof handleTestStepStatsResponse === 'function') {
//                     handleTestStepStatsResponse(response);
//                 }
//                 // handleTestStepStatsResponse(response);
//             }
//         } else {
//             console.log("XHR status else : " + xhr.status);
//         }
//     };
//     xhr.send();
// };


// function handleTestStepStatsResponse(response) {
//     console.log("Callback for testStepDetails invoked from getTestStepStats: " + response);
//     console.log("Response PK: " + response.pk);
//     autoReloadDetailView(response.pk);
// };



function getTestStepStats(formValues) {
    // function getTestStepStats(formValues) {
        console.log("Inside getTestStepStats : " + formValues);
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
                console.log("XHR status if : " + xhr.status);
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    console.log("Response received parsed : " + response);
                    console.log("Response received parsed : " + JSON.stringify(response));
                    handleTestStepStatsResponse(response);
                }
            } else {
                console.log("XHR status else : " + xhr.status);
            }
        };
        xhr.send();
    };


function handleTestStepStatsResponse(response) {
    console.log("Callback for testStepDetails invoked from getTestStepStats: " + response);
    console.log("Response PK: " + response.pk);
    // autoReloadDetailView(response.pk);
    // autoReloadDetailView(response);
    testStepDetails(response);
};


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
        // autoReloadDetailView();
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

function autoReloadDetailView(pk) {
// function autoReloadDetailView(pk) {
    const xhr = new XMLHttpRequest();
    console.log("Inside the autoreload");
    const url = '/testcase/teststep_detail/' + pk + '/'
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const jsonResponse = JSON.parse(xhr.responseText);
                document.getElementById('teststep-container').innerHTML = "JS return " + xhr.responseText + "====";
                testStepDetails(jsonResponse);
            } else {
                console.log('Status : ' + xhr.status);
            }
        }
    }
    xhr.send();
}


/**
 * Display the status for the test step submitted
 */
function testStepDetails(jsonResponse) {
    console.log("Response received in teststepdetails: " + jsonResponse);
    console.log("Type teststepdetails: " + typeof jsonResponse);
    const ctx = document.getElementById('myChart-0');

    console.log("Chart: " + ctx.chart);
    // Check if a chart already exists
    if (ctx && ctx.chart) {
        // Destroy the existing chart
        ctx.chart.destroy();
    }
    const testCases = jsonResponse;
    console.log("Test Cases: " + JSON.stringify(testCases));
    console.log("Tets Case type : " + typeof testCases);
    console.log("Test Cases: " + typeof testCases.num_tc_associated);
    console.log("Test Cases type: " + typeof JSON.parse(testCases.num_tc_associated));

    // ##############################
    // CHART 1
    // ##############################
    const cqIDSet = [];
    const dateSet = new Set();

    const numTCs = JSON.parse(testCases.num_tc_associated);
    console.log("numTCs type: " + typeof numTCs);
    const dataValues = numTCs.map(testCase => {
        console.log("Element: " + JSON.stringify(testCase));
        console.log("Element: " + typeof testCase.fields.cqid);
        cqIDSet.push(testCase.fields.cqid);
        dateSet.add(new Date(testCase.fields.updated_on).toLocaleDateString());
        return cqIDSet.length; // or any other value you want to assign to each test case
    });
    console.log("CQIDSET: " + [...cqIDSet]);
    console.log("DATESET: " + [...dateSet]);
    console.log("DATAVALUES: " + [...dataValues]);

    const options = {
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              stepSize: 1, // Control the step size between ticks
              min: 0, // Minimum value of the y-axis
              max: 10, // Maximum value of the y-axis
            },
          },
        },
      };

    // Assign the chart instance to ctx.chart property
    ctx.chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: [...dateSet],
            datasets: [{
                label: '# of Test Cases using this step',
                data: dataValues,
                borderWidth: 1,
                barPercentage: 1,
                barThickness: 20,
                maxBarThickness: 30,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1,
                    },
                },
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: (context) => {
                            const index = context.dataIndex;
                            const cqID = cqIDSet[index];
                            const length = dataValues[index];
                            return `CQID: ${cqID} | Total TCs : ${length}`;
                        },
                    },
                },
            },
        },
    });

    // Get the modal element
    // const modal = document.getElementById('canvasModal');
    // // Get the canvas elements
    // // const canvas = document.getElementById('myChart-1');
    // const modalCanvas = document.getElementById('modalCanvas');
    // // Get the close button element
    // const closeButton = document.getElementsByClassName('close')[0];

    // // Function to open the modal and display the canvas
    // function openModal() {
    // modal.style.display = 'block';
    // modalCanvas.getContext('2d').drawImage(ctx.chart.canvas, 0, 0);
    // }
    // Function to open the modal and display the canvas
    // function openModal() {
    //     const modalWindow = window.open("", "Chart Window", "width=800, height=600");
    //     modalWindow.document.write(`<img src="${ctx.chart.canvas.toDataURL()}" alt="Chart">`);
    // }

    // // Function to close the modal
    // function closeModal() {
    // modal.style.display = 'none';
    // }

    // Event listener for canvas click
    // ctx.chart.canvas.addEventListener('click', openModal);

    // // Event listener for close button click
    // closeButton.addEventListener('click', closeModal);

    // ##############################
    // CHART 2
    // ##############################
    const configType = JSON.parse(jsonResponse.data);
    const tcHitInfo = jsonResponse.total_raid_hits + " other Test Cases uses " + configType[0].fields.step.raid;
    console.log("String to print : " + tcHitInfo);
    const tcHitInfoHtml = `<ul><li> 🚀 <strong>${jsonResponse.total_raid_hits}</strong> other Test Cases have <strong>${configType[0].fields.step.raid}</strong><br>with same <strong>and/or</strong> other configurations</li></ul>`;
    const ctx1 = document.getElementById('myp-1');
    ctx1.innerHTML = "";
    ctx1.innerHTML = tcHitInfoHtml;


    // ##############################
    // CHART 3
    // ##############################
    const cqTitle = [];
    const tcIds = numTCs.forEach(tc => {
        cqTitle.push(tc.fields.title + " ( CQ ID : " + tc.fields.cqid + ")");
    });
 
    console.log("String to print : " + cqTitle);
    let strPrint = "<p><strong>List of Test cases with exact step</strong><br></p><ul>";
    let cqData = cqTitle.forEach(id => {
        strPrint += `<li> ⭐ <strong>${id}</strong></li>`;
    });
    strPrint += "</ul>";
    const ctx2 = document.getElementById('myp-2');
    ctx2.innerHTML = "";
    ctx2.innerHTML = strPrint;
}
