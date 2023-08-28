import React, { Component } from 'react'

export default class StudentStateMap extends Component {
  state = {
    user: [
        {"id" : 1, name: "Amitabh", city: "Dhanbad"},
        {"id" : 2, name: "Shweta", city: "Patna"},
        {"id" : 3, name: "Aadya", city: "Bangalore"},
        {"id" : 4, name: "Dhruv", city: "Bangalore"},
    ]
  }
    render() {
        const mappedData = this.state.user.map((user) => {
            return <li>
                ID: {user.id} Name: {user.name} City: {user.city}
            </li>
        })
    return (
      <ul>
        {mappedData}
      </ul>
    )
  }
}
