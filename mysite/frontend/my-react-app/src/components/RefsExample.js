import React, { Component } from 'react'


export default class RefsExample extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ""
        }
        // Creating ref
        this.textInput = React.createRef();
    }


    componentDidMount = () => {
        console.log("From Uncontrolled comp : " + this.textInput.current.value);
        this.textInput.current.focus();
    }

    handleSubmit = e => {
        e.preventDefault();
        console.log("E value in handleSubmit : " + this.textInput.current.value)
        this.setState({value: this.textInput.current.value})
    }

    render() {
        return (
            <React.Fragment>
                <h2>You entered : {this.state.value}</h2>
                <form action="" onSubmit={this.handleSubmit}>
                    Name_unc: <input type="text" />
                    Password_unc: <input type="text" ref={this.textInput}/>
                    <input type="submit" value="Submit me"/>
                </form>
            </React.Fragment>
        )
    }
}
