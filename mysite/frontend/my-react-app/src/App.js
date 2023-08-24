import React, { Component } from 'react';
import useCustomCounter from "./components/CustomHooks";

class App extends Component {
    componentDidMount() {
        console.log("App mounted")
    }

    componentWillUnmount() {
        console.log("App will unmount")
    }

    render() {
        return (
            <React.Fragment>
                <h1>Hello from App render"</h1>
                <CountNumber />
            </React.Fragment>
        )
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