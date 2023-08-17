import React, {Component} from "react";

class StudentSetStateFunction extends Component {
    constructor(props) {
        super(props);
        this.state = {
            def: "Some def",
            name: this.props.name,
            roll: this.props.roll
        };
    };

    handleClick = () => {
        this.setState(function(state, props) {
            console.log("State : ", state);
            console.log("Props : ", props);
        });
    }

    render() {
        return (
            <div>
                <h1>Hello {this.state.name}</h1>
                <button onClick={this.handleClick}>Click me State Fun</button>
            </div>
        )
    }
}

export default StudentSetStateFunction;