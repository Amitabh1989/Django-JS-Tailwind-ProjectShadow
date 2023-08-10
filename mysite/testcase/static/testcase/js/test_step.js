/* global console */
"use strict";
// let moduleUrlTable = new Map();

// moduleUrlTable.set("io", "io_module");
// moduleUrlTable.set("config", "config");
import { moduleUrlTable } from './moduleUrlMap.js';


/** 
 * Gets the localStorage content and returns the JSON object
 * @param {boolean} [log=true] - If we want to log the content of the cart
*/
function getTestStep(log=false) {
    var testSteps = localStorage.getItem('testSteps');
    if (testSteps === null) {
        testSteps = {};
        testSteps.moduleForm = [];
    } else {
        testSteps = JSON.parse(testSteps);
    }
    if (log) {
        console.log("Test Case dictionary : " + JSON.stringify(testSteps));
    }
    return testSteps;
}

/**
 * Get each module by count
 */
function getModuleByCount() {
    let tcCart = getTestStep().moduleForm;
    if (!Array.isArray(tcCart)) {
        console.error('tcCart is not an array:', tcCart);
        return; // Return or handle the error appropriately
    }
    let moduleByCount = {};
    tcCart.forEach(step => {
        let moduleType = step['module_type'];
        moduleByCount[moduleType] = (moduleByCount[moduleType] || 0) + 1;
    });
    console.log("Module by count : " + moduleByCount);
    return moduleByCount;
}

/** 
 * Gets the localStorage content and returns the JSON object
 * @param {boolean} [log=true] - If we want to log the content of the cart
*/
function getLastTestStep(log=false) {
    let allTestSteps = getTestStep().moduleForm;
    console.log("Last step is : " + allTestSteps[allTestSteps.length -1])
    return allTestSteps[allTestSteps.length -1];
}

/**
 * Takes the content of the cart and displays it in test step pane
 */
function displayTestSteps() {
    var testStepsAll = getTestStep();
    var testSteps = testStepsAll;
    var testStepCart = document.getElementsByClassName("tc-cart");
    // console.log("TC cart fetched : " + JSON.stringify(testSteps));
    testStepCart[0].innerHTML = "";
    let step = null;
    let stepNo = null;
    var stepString = `<div class="mr-1 ml-1 mb-1 rounded-sm">
                        <div class="flex flex-col rounded-sm">`;
    for (let i = 0;  i < testSteps.moduleForm.length; i++) {
        // step = JSON.stringify(testSteps[i]);
        step = testSteps.moduleForm[i];
        console.log("Test Step displayTestSteps : " + step);
        stepNo = i + 1;
        stepString += `
                <div class="flex flex-row hover:scale-105 hover:bg-sky-100">
                    <div class="flex-initial w-96 text-blue-400 text-left text-sm font-bold ml-auto px-5"><span>Test Step ${stepNo} (${step.module_type.charAt(0).toUpperCase()}${step.module_type.slice(1)})</span></div>
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

        // Get module_type
        let moduleType = document.getElementById("module-name");
        console.log("Module Type : " + moduleType.innerText);

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

        // Add module type information in the step object
        formValues["module_type"] = moduleType.innerText.split(" ")[1].toLowerCase();

        console.log("Form Values: " + JSON.stringify(formValues));

        // Retrieve the testSteps from localStorage
        let testStepslocal = getTestStep();
        console.log("Before Update, cart: ", testStepslocal);

        // Check if 'formValues' property exists
        if (!testStepslocal.hasOwnProperty('moduleForm')) {
            // testSteps.moduleForm = [];
            console.log("No JSON objects found to store testStepslocal, creating");
            testStepslocal.moduleForm = [];
            // testSteps.moduleForm.steps = [];
        } else {
            console.log("Found modeleForm : " + JSON.stringify(testStepslocal));
        }

        console.log("testStepslocal:", testStepslocal);
        console.log("testStepslocal.moduleForm:", testStepslocal.moduleForm);
        console.log("testStepslocal.moduleForm.steps:", testStepslocal.moduleForm);

        // Check if the value being submitted is edited or new. And act accordingly
        const submitType = document.getElementById("submit-step");
        if (submitType.value === 'Save Edited Step') {
            console.log("Saving Edited Step");
            console.log(document.querySelector("#module-name").innerHTML.split(" "))
            let formLabel = document.querySelector("#module-name").innerHTML.split(" ");
            const stepNo = parseInt(formLabel[formLabel.length-1]);
            console.log("Step number is: " + stepNo);
            testStepslocal.moduleForm[parseInt(stepNo-1)] = formValues;
            console.log("BEFORE Edited step details : " + JSON.stringify(testStepslocal.moduleForm));
            localStorage.setItem('testSteps', JSON.stringify(testStepslocal));
            console.log("AFTER  Edited step details : " + JSON.stringify(testStepslocal.moduleForm));
            submitType.value = 'Submit Step';
            document.querySelector("#module-name").innerHTML = `Add ${formLabel[1].toUpperCase()}`;
        } else {
            // Append the form values to the 'formValues' array
            testStepslocal.moduleForm.push(formValues);
            console.log("Pushed value to test case cart : " + JSON.stringify(testStepslocal));
        }

        // Update the 'testSteps' in localStorage
        localStorage.setItem('testSteps', JSON.stringify(testStepslocal));
        console.log("Updated cart: " + JSON.stringify(testStepslocal));

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
            let moduleDict = tcDict.moduleForm;
            let stepDict = moduleDict[testStepId - 1];
            stepDict["stepNo"] = testStepId;
            console.log("StepDict : " + JSON.stringify(stepDict));

            // Compose an Ajax request and fetch the module form - from Database
            ajaxEditRequest(JSON.stringify(stepDict));
            // Populate the page with the request

        } else if ($(event.target).is(".delete-step input[type='button']")) {
            // Get the step number from click
            let testStepId = $(event.target).attr('delete-test-step');
            console.log("Test Step " + testStepId + " selected to be deleted");

            // Go to Index in the localStorage testStepList and get the module name
            let tcDict = getTestStep();
            console.log("TcDict : " + tcDict);
            let moduleDict = tcDict.moduleForm;
            console.log("moduleDict : " + moduleDict);
            // let stepDict = moduleDict[testStepId - 1];
            console.log("Deleting elements from index: " + (testStepId-1));
            console.log("Deleting elements : " + moduleDict[testStepId-1]);
            moduleDict.splice(testStepId-1);
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
        const url = '/api/stepstat/?' + queryString;
        console.log('Get Request : ' + url)
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                console.log("XHR status if : " + xhr.status);
                if (xhr.status === 200) {
                    // console.log("OUTPUT seen : " + xhr.responseText);
                    const response = JSON.parse(xhr.responseText);
                    // console.log("Response received parsed : " + response);
                    // console.log("Response received parsed : " + JSON.stringify(response));
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
    // console.log("Response PK: " + response.pk);
    // autoReloadDetailView(response.pk);
    // autoReloadDetailView(response);
    testStepDetails(response);
};


// /**
//  * Adding module form container to display all modules in the same page
//  * 
//  * @param {*} name 
//  * @returns 
//  */

// function loadModule(appName) {
//     $.ajax({
//         url: '/path/to/module/view/',
//         method: 'GET',
//         data: { app: appName },
//         success: function(response) {
//             $('#form-container').html(response);
//         }
//     });
// }


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
    let testSteps = getTestStep();
    // console.log("Test Steps are : " + JSON.stringify(testSteps));

    // // make a AJAX request
    $.ajax({
        // url: '/testcase/api/',
        url: '/api/stepstat/',
        method: "POST",
        data: JSON.stringify(testSteps),
        // data: testSteps,
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
 function ajaxEditRequest(stepDict) {
    console.log("Creating AJAX request now : " + stepDict);
    // const url = '/api/' + JSON.parse(stepDict).module_type;
    const url = '/' + moduleUrlTable.get(JSON.parse(stepDict).module_type) + '/form';
    console.log("Path is : " + url);
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        editStepFormHandler(xhttp, stepDict);
        // autoReloadDetailView();
    };
    // Modify the URL by appending query parameters
    // const url = '/myapp/?is_ajax=True&send_data=True';
    xhttp.open('GET', url);
    xhttp.send();
}


/**
 * Handles the ajaxEditRequest onload functionality
 * @param {*} xhttp : The XMLHttpRequest object
 * @param {*} stepDict : The step dict of the selected step
 */
function editStepFormHandler(xhttp, stepDict) {
    console.log("Status   : " + xhttp.status);
    // console.log("Context data received : " + xhttp.responseText);
    // console.log("Response : " + xhttp.responseText);
    if (xhttp.status >= 200 && xhttp.status < 300) {
        // const context_data = JSON.parse(xhttp.responseText);
        const context_data = xhttp.responseText;
        const formToLoad = context_data.form;

        console.log("Successfull : ");
        document.getElementById('module-form-container').innerHTML = context_data;
        document.getElementById('submit-step').value = 'Save Edited Step';
        console.log("Finding the Edit the step DOM : " + document.querySelector('.module-name').innerHTML);
        const stepDictParsed = JSON.parse(stepDict);
        document.querySelector('.module-name').innerHTML = `Edit ${stepDictParsed.module_type} : step ${stepDictParsed["stepNo"]}`;
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
    console.log("Response received in teststepdetails: " + JSON.stringify(jsonResponse));
    console.log("Type teststepdetails: " + typeof jsonResponse);

    // console.log("Chart: " + ctx.chart);
    // // Check if a chart already exists
    // if (ctx && ctx.chart) {
    //     // Destroy the existing chart
    //     ctx.chart.destroy();
    // }
    const testCases = jsonResponse;

    if (testCases.exact_test_step && testCases.exact_test_step.length === 0) {
        console.log("List is empty!");
        let chartContainer = document.getElementById("myChart-0");
        chartContainer.innerHTML = "";
        chartContainer.innerHTML = `This is a unique step`;
    } else {
        console.log("Exact Step num TCs   : " + testCases.exact_test_step[0].test_cases.length);
        console.log("Similar Step num TCs : " + testCases.similar_test_step.length);

        // ########################################################
        // CHART 1 : Number of Test Cases using exact step by date
        // ########################################################
        let exactStep_tcs = testCases.exactStep_testCases;
        console.log("Exact Step TCs : " + exactStep_tcs);
        console.log("numTCs type: " + typeof exactStep_tcs);
        let countByDate = {};

        exactStep_tcs.forEach(entry => {
            let _date = new Date(entry["updated_on"]).toLocaleDateString();
            console.log("Entry is : " + _date);
            countByDate[_date] = (countByDate[_date] || 0) + 1;
        });
        console.log("Count by date : " + JSON.stringify(countByDate));

        stepUsageChart(countByDate);
    }


    // #################################
    // CHART 2 : Similar test cases hits
    // #################################
    const similarStep_Tcs = jsonResponse.similarStep_testCases;
    const tcHitInfo = similarStep_Tcs.length + " other Test Cases uses " + getLastTestStep()[jsonResponse["search_key"]].charAt(0).toUpperCase() +
                getLastTestStep()[jsonResponse["search_key"]].slice(1);
        // console.log("String to print : " + tcHitInfo);
        const tcHitInfoHtml = `<ul><li> 🚀 <strong>${similarStep_Tcs.length}</strong> other Test Cases uses <strong>${getLastTestStep()[jsonResponse["search_key"]].charAt(0).toUpperCase()
                + getLastTestStep()[jsonResponse["search_key"]].slice(1)}</strong><br>with different params</strong></li></ul>`;
        const ctx1 = document.getElementById('myp-1');
        ctx1.innerHTML = "";
        ctx1.innerHTML = tcHitInfoHtml;


    // ##############################
    // CHART 3
    // ##############################
    const cqTitle = [];
    let strPrint = "<p><strong>List of Test cases with exact step</strong><br></p><ul>";
    // numTCs = numTCs
    if (jsonResponse.exactStep_testCases && jsonResponse.exactStep_testCases.length > 0) {
        jsonResponse.exactStep_testCases.forEach(tc => {
            cqTitle.push(tc.title + " ( CQ ID : " + tc.cqid + ")");
        });
        // console.log("String to print : " + cqTitle);

        cqTitle.forEach(id => {
            strPrint += `<li> ⭐ ${id}</li>`;
        });
    } else {
        strPrint += `<li class="ml-1 text-sm text-gray-500"> ⭐ <strong>This is a Unique Step from your records...Congrats!</strong></li>`;
    }

    strPrint += "</ul>";
    const ctx2 = document.getElementById('myp-2');
    ctx2.innerHTML = "";
    ctx2.innerHTML = strPrint;

    testCaseDoughNut();
}

function testCaseDoughNut() {
    // ######################################################################
    // CHART 4 : Doughnutchart : Distribution of the modules in a test case
    // ######################################################################
    // Get each module by count.
    const ctx4 = document.getElementById('myChart-2');
    let moduleByCount =getModuleByCount();
    console.log("Doughnut : " + JSON.stringify(getModuleByCount()));
    const DATA_COUNT = moduleByCount.length;
    console.log("Keys   : " + Object.keys(moduleByCount));
    console.log("Values : " + Object.values(moduleByCount));
    const NUMBER_CFG = {count: DATA_COUNT, min: 0, max: 100};

    const data = {
    labels: Object.keys(moduleByCount),
    datasets: [
        {
        label: 'Number of Steps',
        data: Object.values(moduleByCount),
        backgroundColor: ['Red', 'Orange', 'Yellow', 'Green', 'Blue'],
        }
    ]
    };
    // Check if a chart already exists
    if (ctx4 && ctx4.chart) {
        // Destroy the existing chart
        ctx4.chart.destroy();
    }
    console.log("Context chart : " + JSON.stringify(data));
    ctx4.chart = new Chart(ctx4, {
        type: 'doughnut',
        data: data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Your Test case composition'
            }
          }
        },
      }
    );
    }



function stepUsageChart(countByDate) {
    const ctx = document.getElementById('myChart-0');
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
    console.log("Chart: " + ctx.chart);
    // Check if a chart already exists
    if (ctx && ctx.chart) {
        // Destroy the existing chart
        ctx.chart.destroy();
    }
    // Assign the chart instance to ctx.chart property
    ctx.chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(countByDate),
            datasets: [{
                label: '# of TCs using exact step',
                data: Object.values(countByDate),
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
            // plugins: {
            //     tooltip: {
            //         callbacks: {
            //             label: (context) => {
            //                 const index = context.dataIndex;
            //                 const cqID = cqIDSet[index];
            //                 const length = dataValues[index];
            //                 return `CQID: ${cqID} | Total TCs : ${length}`;
            //             },
            //         },
            //     },
            // },
        },
    });
}