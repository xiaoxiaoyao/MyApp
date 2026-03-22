//ReactGreeter.js
import React, {Component} from 'react'
import config from './config.json';

class ReactGreeter extends Component{
  render() {
    return (
      <div>
        "//ReactGreeter.js"
        {config.greetText}
      </div>
    );
  }
}

export default ReactGreeter