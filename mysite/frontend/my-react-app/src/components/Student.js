import React, { Component } from "react";

class Student extends Component {
    state = {
        "name": "Amitabh",
        "roll": this.props.roll
    }
    render() {
        return (
            <h1>
                Hello, {this.state.name}, your roll number is {this.state.roll}
            </h1>
        );
    }
}

export default Student;