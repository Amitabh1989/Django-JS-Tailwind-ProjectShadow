
console.log("Logout JS called");
document.addEventListener("DOMContentLoaded", function() {
  // Get the "Logout" link element by its ID
  const logoutLink = document.getElementById("logout-link");

  // Add a click event listener to the "Logout" link
  logoutLink.addEventListener("click", function(event) {
    event.preventDefault(); // Prevent the default behavior of the link (i.e., navigating to the href)
    console.log("Logout JS clicked");
    // Create a dynamic form element
    const form = document.createElement("form");
    form.method = "POST"; // Set the method to POST
    form.action = "/auth/logout/"; // Set the URL for the logout view

    // Fetch the CSRF token from the cookie
    const csrfToken = getCookie("csrftoken"); // Implement the function getCookie to extract the token


    // Create a CSRF token input field
    const csrfTokenInput = document.createElement("input");
    csrfTokenInput.type = "hidden";
    csrfTokenInput.name = "csrfmiddlewaretoken";
    csrfTokenInput.value = csrfToken;

    // Append the CSRF token input field to the form
    form.appendChild(csrfTokenInput);

    // Append the form to the document body
    document.body.appendChild(form);

    // Submit the form
    console.log("Form is : " + form);
    form.submit();
  });
});

// Function to extract the value of a cookie by name
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}