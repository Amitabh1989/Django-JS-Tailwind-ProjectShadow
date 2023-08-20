import React, { Component } from 'react';
import StudentChildCompLifeCycle from './StudentChildCompLifeCycle';

export default class StudentCompLifeCycle extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: props.name,
            age: props.age
        };
        console.log("Constructor has been called");
    }

    static getDerivedStateFromProps(props, state) {
        console.log("getDerivedStateFromProps called : Props are  : " + JSON.stringify(props));
        console.log("getDerivedStateFromProps called : States are : " + JSON.stringify(state));
        return null;
    }

    handleClick = () => {
        console.log("Handle click called");
    }

    render() {
        console.log("Render called");
        return (
            <div>
                <h1>Hey {this.state.name}, your age is {this.state.age}</h1>
                <StudentChildCompLifeCycle name="Suman" />
            </div>
        );
    }
}
