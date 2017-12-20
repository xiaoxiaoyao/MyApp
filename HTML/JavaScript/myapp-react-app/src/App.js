import React, { Component } from 'react';
import './App.css';
import HelloReact from './components/HelloReact.js'
import HelloReactToDoList from './components/ToDoList.js'

class App extends Component{
  render(){
    return(
    <div>
      <h1>HelloReact 入门程序：</h1>
        <HelloReact name="yao" id="test" num={1} />
      <h1>React 做个ToDoList：</h1>
        <HelloReactToDoList things={[
        {
          task: "one",
          done: true
        },
        {
          task: "two",
          done: false
        },
        {
          task: "three",
          done: false
        }
      ]} />
    </div>
        )
  }
}

export default App;