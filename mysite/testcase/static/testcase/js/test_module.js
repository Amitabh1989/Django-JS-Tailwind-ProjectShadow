/**
 * Adding module form container to display all modules in the same page
 * 
 * @param {*} name 
 * @returns 
 */

function loadModule(appName) {
    console.log("Clicked : " + appName);
    console.log("Clicked after edit : " + appName);
    const url = '/api/' + appName;
    console.log("Path is : " + url);
    $.ajax({
        url: url,
        method: 'GET',
        data: { app: appName },
        success: function(response) {
            $('#module-form-container').html('');
            $('#module-form-container').html(response);
        }
    });
    console.log("Ready");
}


$( document ).ready(loadModule);