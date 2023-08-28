import React, { Component } from 'react'

export default class User_2 extends Component {
  render() {
    return (
      <div>
            <p>ID: {this.props.value.id}</p>
            <p>Name: {this.props.value.name}</p>
            <p>City: {this.props.value.city}</p>
      </div>
    )
  }
}
