import React, { Component } from 'react';

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
  
  export default HelloReactToDoList;  