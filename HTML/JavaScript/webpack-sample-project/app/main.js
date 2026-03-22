//main.js 
const greeter = require('./Greeter.js');
document.querySelector("#root").appendChild(greeter());

//修改main.js如下，使用ES6的模块定义和渲染Greeter模块
import React from 'react';
import {render} from 'react-dom';
import ReactGreeter from './ReactGreeter';

render(<ReactGreeter />, document.getElementById('root'));
