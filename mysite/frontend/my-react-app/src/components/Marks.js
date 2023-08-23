import React, { Component } from 'react';

export default class Marks extends Component {
    constructor(props) {
        super(props);
        console.log("Child Marks class constructor called")
        this.state = {
            mmarks: this.props.mmarks
        };
    }

    static getDerivedStateFromProps(props, state) {
        console.log("Child Marks class getDerivedStateFromProps called")
        if (props.mmarks !== state.mmarks) {
            return {mmarks: props.mmarks}
        }
        return null;
    }



    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log("Child Component Snapshotcalled, called before update in DOM was done");
        console.log("Snapshot PrevProps ", prevProps);
        console.log("Snapshot PrevState ", prevState);
        return 45;
    }

    componentDidMount() {
        console.log("Child Component did mount called, called after update in DOM was done")
    }
    
    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log("Child Component did update called, called after update in DOM was done");
        console.log("CompDidUpdate PrevProps ", prevProps);
        console.log("CompDidUpdate PrevState ", prevState);
        console.log("CompDidUpdate Snapshot  ", snapshot);
    }
    shouldComponentUpdate(nextProps, nextState) {
        if (nextState.mmarks < 1040) {
            console.log("Child class ShouldCompUpdate");
            console.log("NextProps : ", nextProps, " NextState : ", nextState);
            return true;
        }
        console.log("False NextProps : ", nextProps, " NextState : ", nextState);
        return false;
    }

    render() {
        console.log("Child Render called")
        return (
            <div>
                <h1>Marks is {this.state.mmarks}</h1>
            </div>
        )
    }
}