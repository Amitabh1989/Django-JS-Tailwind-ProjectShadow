import React, { Component } from 'react'

export default class ControlledComponents extends Component {
  state = {
    name: ""
  }
  handleClick = (evt) => {
    console.log(evt.target.value)
    this.setState({ name: evt.target.value})
  }
  render() {
    return (
      <div>
        <form action="">
            <label htmlFor="">
                {/* Name: <input type="text" value={this.state.name} onChange={this.handleClick} /> */}
                Name: <textarea value={this.state.name} onChange={this.handleClick} width="100px" />
            </label>
            <br />
        </form>
      </div>
    )
  }
}
