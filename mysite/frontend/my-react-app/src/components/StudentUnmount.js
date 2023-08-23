import React, { Component } from 'react';

export default class StudentUnmount extends Component {
    componentDidMount() {
        console.log("Student mounted")
    };
    render() {
        return (
            <h1>Hello Student</h1>
        )
    }
};
