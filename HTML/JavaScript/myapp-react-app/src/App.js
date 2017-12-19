import React, { Component } from 'react';
import './App.css';
class HelloReactToDoList extends Component{
  constructor(props) {
    super(props);
    this.state = {
      things:props.things
    };
    this.addTodo = this.addTodo.bind(this);
  };
  addTodo() {
    console.log("add todo.",this);
    console.log(this.props);
    const todo = document.getElementById("ToDoList").value;
    // document.getElementById("ToDoList").value = "";
    this.setState({
      things: this.state.things.concat({
        task: todo,
        done: false
      })
    });
  }
  render(){
    return (
      <div>
        <input id="ToDoList" type="input" placeholder="input a todo" />
        <button onClick={this.addTodo}>Add Todo（这边用map函数批量生成列表）</button>
        <ul>
        {console.log(this.state)}
        {this.state.things.map(thing => {
            return (
              <li key={thing.task}>
                <input
                  type="checkbox"
                  onClick={() => {thing.done= !thing.done;}}
                  defaultChecked={thing.done}
                />
                <span>{thing.task}</span>
              </li>
            );
        })}
        </ul>
        <p>{this.state.things.filter(thing => !thing.done).length} tasks remain.</p>
      </div>
    )
  }
}
class HelloReact extends Component{
  constructor(props) {
    super(props);
    this.state = {
      name:props.name,
      num:props.num,
      HelloReactStyleObject:{
        color:'red',
        fontSize:'24px'
      }
    };
  };
  handleChange(e) {
      this.setState({
      name: e.target.value,
    });
  }
  render(){
  return (
    <div>
      <h1 className='bgcolor'>welcome to react world!</h1>
      <h2 style={this.state.HelloReactStyleObject}>Hello, React!{this.state.name},The number is {this.state.num}</h2>
      <p>your name length: {this.state.name.length}.</p>
      <p>Please input your name:
        <input type="text" placeholder="input plz"  onChange={this.handleChange.bind(this)}  />
      </p>
    </div>
  )};
};
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