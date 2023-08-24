import React, { Component, useState } from 'react';

function StateHook() {
    const [name, setName] = useState("Amitabh");
    const [flip, setFlip] = useState(false);

    const handleEvent = () => {
        if (!flip) {
            setName("Shweta");
        } else {
            setName("Amitabh");
        }
        setFlip(!flip);
    }

    return(
        <div>
            <h1>{name}</h1>
            <button onClick={handleEvent}>Click to change</button>
        </div>
    )
}

export default StateHook;