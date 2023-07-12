/**
 * Adding module form container to display all modules in the same page
 * 
 * @param {*} name 
 * @returns 
 */

let moduleUrlTable = new Map();

moduleUrlTable.set("io", "io_module");
moduleUrlTable.set("config", "config");


function loadModule(appName="config") {
    console.log("Clicked : " + appName);
    console.log("Clicked after edit : " + appName);
    const url = '/' + moduleUrlTable.get(appName) + '/form/';
    console.log("Path is : " + url);
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log("Calling : " + url);
        console.log("Calling : " + this.responseText);
        document.getElementById('module-form-container').innerHTML = "";
        document.getElementById('module-form-container').innerHTML = this.responseText;
    }
    xhttp.open('GET', url);
    xhttp.send();
    console.log("Ready");
}


// $( document ).ready(loadModule);
window.onload = function() {
    loadModule();
};


    // $.ajax({
    //     url: url,
    //     method: 'GET',
    //     data: { app: appName },
    //     success: function(response) {
    //         $('#module-form-container').html('');
    //         $('#module-form-container').html(response);
    //     }
    // });