import React, { Component, useState } from 'react';
import Guest from './Guest';

// export default class User extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             loggedIn: this.props.loggedIn
//         }
//     }

//     handleLogout = () => {
//         console.log("Hanlding Logout")
//         this.setState({loggedIn: false})
//     }

//     render() {
//         if (this.props.loggedIn) {
//             return (
//                 <React.Fragment>
//                     <h1>Hi, i am logged in</h1>
//                     <button onClick={this.handleLogout}>Logout</button>
//                 </React.Fragment>
//             )
//         }
//         return (
//             <Guest loggedIn={false} />
//         )
//     }
// }

export default class User extends Component {
    render() {
        return (
            <React.Fragment>
                Hello Amitabh
                <button onClick={this.props.clickData}>Logout</button>
            </React.Fragment>
        )
    }
}