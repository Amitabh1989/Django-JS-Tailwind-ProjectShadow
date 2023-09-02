import React, { Component } from 'react'

export default class MultiControlledComponent extends Component {
    state = {
        name: "",
        password: ""
    }

    handleChange = (evt) => {
        const val = 
            evt.target.name === "password"
                ? evt.target.value.toUpperCase().substr(0, 10)
                : evt.target.value;
            this.setState({ [evt.target.name]: val })
    };

    handleSubmit = (evt) => {
        console.log("Event is : ", evt);
        evt.preventDefault();
    }
    render() {
    return (
      <div>
        <form action="" onSubmit={this.handleSubmit}>
            <label htmlFor="">
                Name: <input type="text" value={this.state.name} name="name" onChange={this.handleChange} />
            </label>
            <br />
            <label htmlFor="">
                Password: <input type="text" value={this.state.password} name="password" onChange={this.handleChange} />
            </label>
            <button>Submit</button>
        </form>
      </div>
    )
  }
}
