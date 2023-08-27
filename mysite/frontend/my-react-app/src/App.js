import React, { Component } from 'react';
import useCustomCounter from "./components/CustomHooks";
import User from './user/User';
import Guest from './user/Guest';

class App extends Component {
    componentDidMount() {
        console.log("App mounted")
    }

    componentWillUnmount() {
        console.log("App will unmount")
    }

    // handleLogout = () => {
    //     console.log("Hanlding Logout")
    //     this.setState({loggedIn: false})
    // }

    render() {
        const isRegistered = this.props.consumer
        const isPrime = this.props.isPrime
        if (isRegistered) {
            return (
                <React.Fragment>
                    {/* <User loggedIn={true} /> */}
                    {/* <button onClick={this.handleLogout}>Logout</button> */}
                    <h1>Hello from App render"</h1>
                    {isPrime && <User loggedIn={true} />}
                    <CountNumber />
                </React.Fragment>
            )
        }
        return <Guest loggedIn={false} />
    }
}

function CountNumber() {
    const count = useCustomCounter();
    const count1 = useCustomCounter();

    return(
        <React.Fragment>
            <h1>CusotmHook Count {count.count}</h1>
            <button onClick={count.handleCount}>Count up</button>

            <h1>CusotmHook Count {count1.count}</h1>
            <button onClick={count1.handleCount}>Count up</button>
        </React.Fragment>
    )
}

// export { App, CountNumber };
export default App;