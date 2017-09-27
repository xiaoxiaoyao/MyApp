// ==UserScript==
// @name         JD-auto-checkIn
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  彻底解决下班忘记打卡烦恼，开着页面就每隔3.3分钟自动打一次卡
// @author       xiaoxiaoyao
// @match        http://jdwe.jd.com/
// @grant        none
// @supportURL   https://github.com/xiaoxiaoyao/PythonApplication1/issues
// ==/UserScript==

(function() {
    'use strict';
    
    // Your code here...
    setInterval(function(){
        //要执行的代码
        checkIn();
    },200000);

    location.reload([bForceGet]);
})();
