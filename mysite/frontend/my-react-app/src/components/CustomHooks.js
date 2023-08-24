import { useState } from "react";

function useCustomCounter() {
    const [count, setCount] = useState(0);

    const handleCount = () => {
        setCount(count+1);
    }

    return {
            count,
            handleCount
    }
}

export default useCustomCounter;