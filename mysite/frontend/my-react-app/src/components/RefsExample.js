import React, { Component } from 'react'


export default class RefsExample extends Component {
    constructor(props) {
        super(props);
        // Creating ref
        this.textInput = React.createRef();
    }

    handleSubmit = e => {
        e.preventDefault();
    }

    componentDidMount = () => {
        console.log("From Uncontrolled comp : " + this.textInput.current.value);
        this.textInput.current.focus();
    }

    render() {
        return (
            <form action="" >
                Name_unc: <input type="text" />
                Password_unc: <input type="text" ref={this.textInput}/>
            </form>
        )
    }
}
