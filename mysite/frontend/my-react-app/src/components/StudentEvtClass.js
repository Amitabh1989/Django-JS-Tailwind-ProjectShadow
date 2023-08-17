import React, { Component } from "react";


// EXAMPLE USING ARROW FUNCTION

// class StudentEvtClass extends Component {
//     constructor(props){
//         super(props);
//         this.state = {
//             "name": "Amitabh",
//             "city": this.props.city
//         };
//     }

//     handleClick = () => {
//         console.log("Hello " + this.state.city);
//         console.log("Hello ", this);
//         document.getElementById("btnNew").innerText = this.state.city;
//     }

//     render() {
//         return (
//             <div>
//                 <h1>Say hello!</h1>
//                 <button onClick={this.handleClick} id="btnNew">Reveal City</button>
//             </div>
//         );
//     }
// }

// export default StudentEvtClass;

// ===========================================================================

// EXAMPLE USING SUPER BIND METHOD
class StudentEvtClass extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "Amitabh",
            city: this.props.city
        };
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick() {
        console.log("Clicked ", this);
        document.getElementById("btnNew").innerText = this.state.city;
    }

    render() {
        return(
            <React.Fragment>
                <h1>Hey Amitabh - class</h1>
                <h3>Class Based Event handling</h3>
                <button onClick={this.handleClick} id="btnNew">Reveal City</button>
            </React.Fragment>
        )
    }
}

export default StudentEvtClass;