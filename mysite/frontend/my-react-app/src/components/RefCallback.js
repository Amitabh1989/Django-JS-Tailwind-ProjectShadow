import React, { Component } from 'react'
import LiftStateUp from './LiftStateUp';

export default class RefCallback extends Component {
  constructor() {
    super();
    this.state = {
        name: "Hey BUddddyyyy"
    }
    this.refCallback = null;
    this.setrefCallback = element => {
        this.refCallback = element;
    }
  }

  componentDidMount = () => {
    if(this.refCallback) {
        this.refCallback.focus();
    }
  }

  render() {
    return (
      <div>
        Name_callback : <input type="text" />
        Password_callaback : <input type="text" ref={this.setrefCallback} />
        AddressCallback : <input type="text" />
        <LiftStateUp name={this.state.name}/>
      </div>
    )
  }
}
