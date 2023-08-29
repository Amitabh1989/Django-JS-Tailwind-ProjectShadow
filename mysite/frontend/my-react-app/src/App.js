import React, { Component } from 'react'
import User_2 from './user/User_2';


// JS OUTSIDE RETURN STATEMENT
// export default class App extends Component {
//     render() {
//         const arr = [10, 20, 30 , 40];
//         const newArr = arr.map(num => {
//             return <li>{num*2}</li>
//         });
//     return (
//       <div>{newArr}</div>
//         )
//     }
// }



// JS INSIDE RETURN STATEMENT
// export default class App extends Component {
//     render() {
//         const arr = [10, 20, 30 , 40];
//         return (
//             <ul>
//                 {
//                     arr.map(num => {
//                         return <li>{num * 2}</li>
//                     })
//                 }
//             </ul>
//         )
//     }
// }


// // TAKING ARR VAL FROM PROPS
// export default class App extends Component {
//     render() {
//         const arr = this.props.arr;
//         return (
//             <ul>
//                 {
//                     arr.map(num => {
//                         return <li>{num * 2}</li>
//                     })
//                 }
//             </ul>
//         )
//     }
// }


// PASSING PROPS TO USER MODULE TO LIST OUT USERS, WITH KEY
export default class App extends Component {
    state = {
        user: [
            {"id" : 1, name: "Amitabh", city: "Dhanbad"},
            {"id" : 2, name: "Shweta", city: "Patna"},
            {"id" : 3, name: "Aadya", city: "Bangalore"},
            {"id" : 4, name: "Dhruv", city: "Bangalore"},
        ],
        changeStyle: false
      }
    clickHandle = () => {
        if (this.state.changeStyle) {
            this.setState({changeStyle: false})
        } else {
            this.setState({changeStyle: true})
        }
    }
  render() {
    const userData = this.state.user;
    const btnStyle = {
        color: "red",
        backgroundColor: "blue"
    }
    if (this.state.changeStyle) {
        btnStyle.color = "white"
    } else {
        btnStyle.color = "red"
    }
    return (
      <div>
        <ul>
            {
                userData.map((user) => 
                    (
                        <React.Fragment>
                            <li key={user.id}>ID: {user.id} Name: {user.name} City : {user.city}</li>
                            <User_2 value={user}/>
                            <button style={btnStyle} onClick={this.clickHandle}>Click to change</button>
                        </React.Fragment>
                    ))
            }
        </ul>
      </div>
    )
  }
}
