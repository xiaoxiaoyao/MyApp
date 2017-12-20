import React, { Component } from 'react';

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


export default HelloReact;