import React from "react";
import ReactDOM from "react-dom";
import Student from "./components/Student";
import StudentConstructor from "./components/StudentConstructor";
import StudentEvtClass from "./components/StudentEvtClass";
import StudentEvtFunction from "./components/StudentEvtFunction";
import StudentEvtFunPreventDefault from "./components/StudentFunEvtPreventDefault";
import StudentSetState from "./components/StudentState";
import StudentSetStateFunction from "./components/StudentSetStateFunction";

// Rendering Component

ReactDOM.render(<Student roll="102" />, document.getElementById("root"));
ReactDOM.render(<StudentEvtClass city="Dhanbad" />, document.getElementById("root"));


// Create a new elemnent to render this
const newDiv = document.createElement("div");
newDiv.setAttribute("id", "newDivId");
document.body.appendChild(newDiv);
ReactDOM.render(<StudentConstructor roll="104"/>, document.getElementById("newDivId"));


// Create a new element for function div
const functionDiv = document.createElement("div");
functionDiv.setAttribute("id", "funDivBuddy");
document.getElementById("root").appendChild(functionDiv);
ReactDOM.render(<StudentEvtFunction city="Bokaro" name="Amitabh - function"/>, document.getElementById("funDivBuddy"));

// Create a new element for prevent default
const preventDiv = document.createElement("preventDiv");
preventDiv.setAttribute("id", "preventDiv");
document.getElementById("root").appendChild(preventDiv);
ReactDOM.render(<StudentEvtFunPreventDefault name="Amitabh - preventDef" city="Ranchi"/>, document.getElementById("preventDiv"));


// Create new element for student set state
const setStateDiv = document.createElement("setStateDiv");
setStateDiv.setAttribute("id", "setStateDiv");
document.getElementById("root").appendChild(setStateDiv);
ReactDOM.render(<StudentSetState name="Amitabh - SetState" city="Bokaro"/>, document.getElementById("setStateDiv"));


// Create new element for demo of Function in SetState
const newDivState = document.createElement("div");
newDivState.setAttribute("id", "newDivState");
document.getElementById("root").appendChild(newDivState);
ReactDOM.render(<StudentSetStateFunction name="Aadu Mera Dil" roll="1" />, document.getElementById("newDivState"));