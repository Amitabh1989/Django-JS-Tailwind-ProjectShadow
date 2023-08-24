// Use Effect is used for API calls, dataq fetching, changing document heading and etc
// Its basically called at each and every render. First render and after every update
// Like in class component lifecycle we had ComponentDidMount, ComponentDidUpdate and 
// ComponentWillUnmount, all these 3 functionalities are handled by useEffect for
// functional JS.

// Note how all 3 class lifecycle states happen after render pahse, so all functionality that
// can happen after render, can be done using useEffect

import React, { useEffect, useState } from 'react';

function StateEffect() {
    const [countUp, setCountUp] = useState(0);
    const [countDown, setcountDown] = useState(50);

    const increment = () => {
        setCountUp(countUp+1)
    }

    const decrement = () => {
        setcountDown(countDown+1)
    }

    useEffect(() => {
        console.log("useEffect called");
    }, [countUp]);

    return(
        <React.Fragment>
            <h1>Count Up : {countUp}</h1>
            <button onClick={increment}>Count Up</button>

            <h1>Count Down : {countDown}</h1>
            <button onClick={decrement}>Count Down</button>
        </React.Fragment>
    )
}

export default StateEffect;