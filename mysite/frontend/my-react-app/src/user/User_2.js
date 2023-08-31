import React, { Component } from 'react';
import "../App.css"
import styles from "./User.module.css";

export default class User_2 extends Component {
  render() {
    return (
      <div>
            <p className={styles.txt}>ID: {this.props.value.id}</p>
            <p>Name: {this.props.value.name}</p>
            <p>City: {this.props.value.city}</p>
      </div>
    )
  }
}
