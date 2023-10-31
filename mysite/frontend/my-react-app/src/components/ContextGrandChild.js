import React, { Component } from 'react';
import { MyContext } from './ContextParent';

export default class ContextGrandChild extends Component {
  render() {
    return (
      <MyContext.Consumer>
        {data => <h3>I am from GrandChild {data.user} -- {data.age}</h3>}
      </MyContext.Consumer>
    );
  }
}
