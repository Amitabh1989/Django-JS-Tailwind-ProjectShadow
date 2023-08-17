import React, {Component} from "react";

// USING SIMPLE FUNCTION
// function StudentEvtFunction(props) {
//     function handleClick() {
//         console.log("Hey man");
//         document.getElementById("buddyBtn").innerText = props.city;
//     }

//     return (
//         <div id="newDivBuddy">
//             <h1>Hello {props.name}</h1>
//             <h3>Function Based Event handling</h3>
//             <button onClick={handleClick} id="buddyBtn">Click me</button>
//         </div>
//     );
// }

// export default StudentEvtFunction;


// EXAMPLE USING ARROW FUNCTION
function StudentEvtFunction(props) {
    const handleClick = () => {
        console.log("Clicked function based evt handler");
        document.getElementById("btnBudy").innerText = props.city;
    };

    return (
        <div>
            <h1>Hello {props.name}</h1>
            <button onClick={handleClick} id="btnBudy">Click me arrow fun</button>
        </div>
    )
}

export default StudentEvtFunction;