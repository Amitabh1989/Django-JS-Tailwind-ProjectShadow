import React, { Component } from 'react';

export default class Marks extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mmarks: this.props.mmarks
        };
    }

    static getDerivedStateFromProps(props, state) {
        console.log("Child Marks class constructor called")
        if (props.mmarks !== state.mmarks) {
            return {mmarks: props.mmarks}
        }
        return null;
    }

    render() {
        return (
            <div>
                <h1>Marks is {this.state.mmarks}</h1>
            </div>
        )
    }
}