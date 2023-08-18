import React, {Component} from "react";

class StudentEvtArgs extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "Amitabh",
            roll: this.props.roll
        };
    };

    handleClick = (roll, e) => {
        console.log("Button clicked for ID " + roll);
        console.log("Button clicked evt ", e);
    }

    handleClickArg = (e) => {
        this.handleClick(this.state.roll, e)
    }

    render() {
        return(
            <div>
                <h1>Hello {this.state.name} - passing args</h1>
                <button onClick={this.handleClickArg}>Reveal (extra function)</button>
                <button onClick={e => {
                    this.handleClick(this.state.roll, e)
                    }}
                    >
                        Reveal (anonymous function)
                </button>
            </div>
        )
    }
}

export default StudentEvtArgs;