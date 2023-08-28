import React, { Component } from 'react';
import useCustomCounter from "./components/CustomHooks";
import User from './user/User';
import Guest from './user/Guest';

class App extends Component {
    state = {
        isLoggedIn: false
    }
    componentDidMount() {
        console.log("App mounted")
    }

    componentWillUnmount() {
        console.log("App will unmount")
    }

    handleLogin = () => {
        this.setState({isLoggedIn: true})
    }

    handleLogout = () => {
        console.log("Hanlding Logout")
        this.setState({isLoggedIn: false})
    }

    render() {
        const isLoggedIn = this.state.isLoggedIn;
        const isRegistered = this.props.consumer
        const isPrime = this.props.isPrime;
        // let consumer;
        // if (isLoggedIn) {
        //     return (
        //         <React.Fragment>
        //             <h1>Hello from App render"</h1>
        //             {isPrime && <User logOut={this.handleLogout} />}
        //             <CountNumber />
        //         </React.Fragment>
        //     )
        // }

        // CONDITIONAL RENDERING
        // if (isLoggedIn) {
        //     consumer = <User clickData={this.handleLogout} />;
        // } else {
        //     consumer = <Guest clickData={this.handleLogin} />;
        // }
        // return <React.Fragment>{consumer}</React.Fragment>

        // INLINE RENDRING
        // return (
        //     <React.Fragment>
        //         {isLoggedIn ? <User clickData={this.handleLogout} /> : <Guest clickData={this.handleLogin} />}
        //     </React.Fragment>
        // )

        // IIFE method
        return (
            <React.Fragment>
                {
                    (() => {
                        if (isLoggedIn) {
                            return <User clickData={this.handleLogout} />;
                        } else {
                            return <Guest clickData={this.handleLogin} />;
                        }
                    })()
                }
            </React.Fragment>
        );
            
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