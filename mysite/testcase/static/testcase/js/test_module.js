/**
 * Adding module form container to display all modules in the same page
 * 
 * @param {*} name 
 * @returns 
 */

import { moduleUrlTable } from './moduleUrlMap.js';

function loadModule(appName="config") {
    console.log("Clicked : " + appName);
    console.log("Clicked after edit : " + appName);
    const url = '/' + moduleUrlTable.get(appName) + '/form/';
    console.log("Path is : " + url);
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        console.log("Calling : " + url);
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

const moduleList = document.getElementById("module-list");
moduleList.addEventListener('click', function(event) {
    const target = event.target;
    console.log("Target : " + target);
    console.log("Event  : " + event);
    const appName = target.dataset.appname;
    console.log("Target detail : " + appName);
    loadModule(appName);
});