import React from "react";
import ReactDOM from "react-dom";
import Student from "./components/Student";
import StudentConstructor from "./components/StudentConstructor";
import StudentEvtClass from "./components/StudentEvtClass";

// Rendering Component

ReactDOM.render(<Student roll="102" />, document.getElementById("root"));
ReactDOM.render(<StudentEvtClass city="Dhanbad" />, document.getElementById("root"));

// Create a new elemnent to render this
const newDiv = document.createElement("div");
newDiv.setAttribute("id", "newDivId");
document.body.appendChild(newDiv);
ReactDOM.render(<StudentConstructor roll="104"/>, document.getElementById("newDivId"));