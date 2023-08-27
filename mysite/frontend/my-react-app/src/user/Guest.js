import React, { Component, useState } from 'react';

export default class Guest extends Component {
    handleLogin = () => {
        console.log("Handling login")
    }

    handleRegister = () => {
        console.log("Handling Register")
    }
    render() {
        return (
            <React.Fragment>
                <h1>Hi, i am Guest</h1>
                <button onClick={this.handleLogin}>Login</button>
                <button onClick={this.handleRegister}>Register</button>
            </React.Fragment>
        )
    }
}