// ==UserScript==
// @name         JD-auto-checkIn
// @namespace    https://github.com/xiaoxiaoyao/MyApp/
// @version      0.1.2
// @description  解决下班忘记打卡烦恼，开着页面就每隔3.3分钟自动打一次卡，注意半夜也会打卡，只要开机就打卡
// @author       xiaoxiaoyao
// @match        http://erp.jd.com/
// @grant        none
// @supportURL   https://github.com/xiaoxiaoyao/PythonApplication1/issues
// ==/UserScript==

(function() {
    'use strict';
    // Your code here...
    setInterval(function(){checkIn();},980001);
})();