import React, { Component } from "react";

class StudentEvtClass extends Component {
    constructor(props){
        super(props);
        this.state = {
            "name": "Amitabh",
            "city": this.props.city
        };
    }

    handleClick = () => {
        console.log("Hello " + this.state.city);
        document.getElementById("btnNew").innerText = this.state.city;
    }

    render() {
        return (
            <div>
                <h1>Say hello!</h1>
                <button onClick={this.handleClick} id="btnNew">Reveal City</button>
            </div>
        );
    }
}

export default StudentEvtClass;