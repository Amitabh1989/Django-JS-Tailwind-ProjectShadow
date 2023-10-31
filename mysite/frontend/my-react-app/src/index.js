import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
// import StudentUnmount from "./components/StudentUnmount";
// import Student from "./components/Student";
import StudentConstructor from "./components/StudentConstructor";
// import StudentEvtClass from "./components/StudentEvtClass";
import StudentEvtFunction from "./components/StudentEvtFunction";
import StudentEvtFunPreventDefault from "./components/StudentFunEvtPreventDefault";
import StudentSetState from "./components/StudentState";
import StudentSetStateFunction from "./components/StudentSetStateFunction";
import StudentEvtArgs from "./components/StudentPassArgsEvtHandler";
import StudentCompLifeCycle from "./components/StudentComponentLifeCycle";
import StudentUpdate from "./components/StudentUpdateDemo";
import StateHook from "./components/UseStateHook";
import StateEffect from "./components/UseEffectHook";
import StateEffectSameButton from "./components/UseEffectHookSameElement";
import StudentStateMap from "./components/StudentStateMap";
import ControlledComponents from "./components/ControlledComponents";
import MultiControlledComponent from "./components/MultiControlledComponent";
import RefsExample from "./components/RefsExample";
import RefCallback from "./components/RefCallback";
import ContextParent from "./components/ContextParent";


// ReactDOM.render(<App consumer={true} isPrime={true}/>, document.getElementById("root"))
const nums = [10, 20, 30, 40];
ReactDOM.render(<App arr={nums}/>, document.getElementById("root"))
// ReactDOM.render(<App arr={[10, 20, 30, 40]}/>, document.getElementById("root"))
// Rendering Component
// ReactDOM.render(<Student roll="102" />, document.getElementById("root"));
// ReactDOM.render(<StudentEvtClass city="Dhanbad" />, document.getElementById("root"));

// Create a new elemnent to render this
const contCompDiv = document.createElement("div");
contCompDiv.setAttribute("id", "contCompDiv");
document.body.appendChild(contCompDiv);
ReactDOM.render(<ControlledComponents />, document.getElementById("contCompDiv"));

// Create a new elemnent to render this
const multiContCompDiv = document.createElement("div");
multiContCompDiv.setAttribute("id", "multiContCompDiv");
document.body.appendChild(multiContCompDiv);
ReactDOM.render(<MultiControlledComponent />, document.getElementById("multiContCompDiv"));


// Create a new elemnent to render this
const newMapDiv = document.createElement("div");
newMapDiv.setAttribute("id", "newMapDiv");
document.body.appendChild(newMapDiv);
ReactDOM.render(<StudentStateMap />, document.getElementById("newMapDiv"));

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
ReactDOM.render(<StudentUpdate marks={1034} />, document.getElementById("mmarks"))


// ReactDOM will unmount
// ReactDOM.render(< App />, document.getElementById("root"));
// ReactDOM.render(< StudentUnmount />, document.getElementById("stu"));
// ReactDOM.unmountComponentAtNode(document.getElementById("root"));


// UseStateHook
const stateHook = document.createElement("stateHook")
stateHook.setAttribute("id", "stateHook")
document.getElementById("root").appendChild(stateHook)
ReactDOM.render(<StateHook />, document.getElementById("stateHook"))


// useEffect StateHook
const effectHook = document.createElement("effectHook")
effectHook.setAttribute("id", "effectHook")
document.getElementById("root").appendChild(effectHook)
ReactDOM.render(<StateEffect />, document.getElementById("effectHook"))

// useEffect StateHook same button
const effectHooksb = document.createElement("effectHooksb")
effectHooksb.setAttribute("id", "effectHooksb")
document.getElementById("root").appendChild(effectHooksb)
ReactDOM.render(<StateEffectSameButton />, document.getElementById("effectHooksb"))

const uncontrollerComp = document.createElement("uncontrollerComp")
uncontrollerComp.setAttribute("id", "uncontrollerComp")
document.getElementById("root").appendChild(uncontrollerComp)
ReactDOM.render(<RefsExample />, document.getElementById("uncontrollerComp"))

const refCallbackDiv = document.createElement("refCallbackDiv")
refCallbackDiv.setAttribute("id", "refCallbackDiv")
document.getElementById("root").appendChild(refCallbackDiv)
ReactDOM.render(<RefCallback />, document.getElementById("refCallbackDiv"))


const contextDiv = document.createElement("contextDiv")
contextDiv.setAttribute("id", "contextDiv")
document.getElementById("root").appendChild(contextDiv)
ReactDOM.render(<ContextParent />, document.getElementById("contextDiv"))