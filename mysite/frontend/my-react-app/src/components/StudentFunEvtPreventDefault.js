import React from "react";

function StudentEvtFunPreventDefault(props) {
    const handleClick = (e) => {
        console.log("Clicked");
        e.preventDefault();
        document.getElementById("hrefPrev").innerText = props.name + " -- " + props.city;
    };

    return (
        <div>
            <h1>Hello {props.name}</h1>
            <a href="www.google.com" onClick={handleClick} id="hrefPrev">Default prevented</a>
        </div>
    )
}

export default StudentEvtFunPreventDefault;