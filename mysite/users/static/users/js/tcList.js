"use strict";
console.log("TC list js called");

document.addEventListener("DOMContentLoaded", function() {

    const tcListUrl = document.getElementById("tcListUrl");

    tcListUrl.addEventListener("click", function(event) {
        event.preventDefault();
        const form = document.createElement("form");
        form.method = "GET";
        form.action = "/testcase/tcs/";
        // Set the desired Accept header in the request
        const headers = new Headers();
        headers.append("Accept", "application/json"); // Change the media type as desired

        const request = new Request(form.action, {
            method: form.method,
            headers: headers
        });
    })
})