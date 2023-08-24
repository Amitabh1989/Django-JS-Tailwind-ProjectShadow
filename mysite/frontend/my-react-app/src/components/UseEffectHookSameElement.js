// Use Effect is used for API calls, dataq fetching, changing document heading and etc
// Its basically called at each and every render. First render and after every update
// Like in class component lifecycle we had ComponentDidMount, ComponentDidUpdate and 
// ComponentWillUnmount, all these 3 functionalities are handled by useEffect for
// functional JS.

// Note how all 3 class lifecycle states happen after render pahse, so all functionality that
// can happen after render, can be done using useEffect

import React, { useEffect, useState } from 'react';

function StateEffectSameButton() {
    const [countUp, setCountUp] = useState(0);
    const [increment, setIncrement] = useState(true);

    const incrementDecrement = () => {
        if (increment) {
            setCountUp(countUp+1)
        } else {
            setCountUp(countUp-1)
        }
    }

    const toggleCounter = () => {
        setIncrement(!increment);
    }

    useEffect(() => {
        if (increment) {
            console.log("useEffect called");
            // Add any other logic you want to run when increment is true
        }
    }, [countUp, increment]);

    return(
        <React.Fragment>
            <h1>Count Me : {countUp}</h1>
            <button onClick={incrementDecrement}>Count {increment ? "Up" : "Down"}</button>
            <button onClick={toggleCounter}>Toggle Counter</button>
        </React.Fragment>
    )
}

export default StateEffectSameButton;