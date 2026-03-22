import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(
    <div>
        <App name="yao" num={0} />
    </div>, document.getElementById('root'));
registerServiceWorker();
