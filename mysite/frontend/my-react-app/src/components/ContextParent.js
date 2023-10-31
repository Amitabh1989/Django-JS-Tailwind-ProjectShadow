import React, { Component } from 'react';
import ContextChild from './ContextChild';
import ContextGrandChild from './ContextGrandChild';

export const MyContext = React.createContext();

export default class ContextParent extends Component {
  render() {
    return (
      <React.Fragment>
        {/* <ContextChild /> */}
        <MyContext.Provider value={{ user: "Amitabh Context", age: 34 }}>
          <ContextGrandChild />
        </MyContext.Provider>
      </React.Fragment>
    );
  }
}