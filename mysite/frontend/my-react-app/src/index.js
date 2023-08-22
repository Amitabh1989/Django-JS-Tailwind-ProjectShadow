import React from "react";
import ReactDOM from "react-dom";
import Student from "./components/Student";
import StudentConstructor from "./components/StudentConstructor";
import StudentEvtClass from "./components/StudentEvtClass";
import StudentEvtFunction from "./components/StudentEvtFunction";
import StudentEvtFunPreventDefault from "./components/StudentFunEvtPreventDefault";
import StudentSetState from "./components/StudentState";
import StudentSetStateFunction from "./components/StudentSetStateFunction";
import StudentEvtArgs from "./components/StudentPassArgsEvtHandler";
import StudentCompLifeCycle from "./components/StudentComponentLifeCycle";
import StudentUpdate from "./components/StudentUpdateDemo";

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

// Create new element for Student Evt Args
const evtArgsDiv = document.createElement("div");
evtArgsDiv.setAttribute("id", "evtArgsDiv");
document.getElementById("root").appendChild(evtArgsDiv);
ReactDOM.render(<StudentEvtArgs roll="120" />, document.getElementById("evtArgsDiv"));


// New Div for StudentComponentLifeCycle
const compLifeCycle = document.createElement("div");
compLifeCycle.setAttribute("id", "compLifeCycle");
document.getElementById("root").appendChild(compLifeCycle);
ReactDOM.render(<StudentCompLifeCycle name="Amitabh" age="29" />, document.getElementById("compLifeCycle"));

// New Div for marks
const mmarks = document.createElement("div")
mmarks.setAttribute("id", "mmarks")
document.getElementById("root").appendChild(mmarks)
ReactDOM.render(<StudentUpdate marks="1034" />, document.getElementById("mmarks"))
