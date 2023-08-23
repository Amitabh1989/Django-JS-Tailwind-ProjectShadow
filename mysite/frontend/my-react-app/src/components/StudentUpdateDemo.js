import React, { Component } from 'react';
import Marks from "./Marks";

export default class StudentUpdate extends Component {
    constructor(props) {
        console.log("Student update class constriuctor called")
        super(props);
        this.state = {
            marks: this.props.marks
        };
    }

    static getDerivedStateFromProps(props, state) {
        console.log("Parent Update class getDerivedStateCalled");
    }

    clickHandler = () => {
        console.log("Clicked");
        // this.setState({marks: "10234"})
        this.setState({marks: this.state.marks+2})
    }

    componentDidMount() {
        console.log("Parent Component did update called")
    }

    render() {
        console.log("Parent Render called")
        return (
            <div>
                {/* <h1>Old Marks {this.state.marks}</h1> */}
                <Marks mmarks={this.state.marks}/>
                <button onClick={this.clickHandler}>Change</button>
            </div>
        )
    };
}