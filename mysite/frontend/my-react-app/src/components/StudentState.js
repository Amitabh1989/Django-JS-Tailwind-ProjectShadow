import React, {Component} from "react";

class StudentSetState extends Component {
    constructor(props) {
        super(props);
        this.state = {
            // name: "Amitabh",
            name: this.props.name,
            city: this.props.city
        };
    }

    handleClick = () => {
        console.log("Setstate clicked");
        this.setState({city: "Sindri", name: "Amitabh - StateChanged"});
        document.getElementById("btnMe").innerText = this.state.city + " -- " + this.state.name;
    };

    render() {
        return (
            <div>
                <h1>Hello {this.state.name}</h1>
                <button onClick={this.handleClick} id="btnMe">Change State</button>
            </div>
        )
    }
}

export default StudentSetState;