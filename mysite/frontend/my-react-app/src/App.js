import React, { Component } from 'react';

export default class App extends Component {
    componentDidMount() {
        console.log("App mounted")
    }

    componentWillUnmount() {
        console.log("App will unmount")
    }

    render() {
        return (
            console.log("Hello from App render")
        )
    }
}

