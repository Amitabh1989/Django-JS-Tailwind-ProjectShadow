import React, { Component } from 'react';

export default class StudentChildCompLifeCycle extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: this.props.name
        };
        console.log("Child class constructor called");
    }

    static getDerivedStateFromProps(props, state) {
        console.log("Child getDerivedStateFromProps called : Props are  : " + JSON.stringify(props));
        console.log("Child getDerivedStateFromProps called : States are : " + JSON.stringify(state));
        return null;
    }

    componentDidMount() {
        // Get data from server and setState. All AJAX query comes here
        console.log("Child Component did mount called")
    }

    render() {
        console.log("Child class Render called");
        return (
            <div>
                <h1>Child class called, {this.state.name}</h1>
            </div>
        );
    }
}
