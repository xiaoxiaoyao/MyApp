// ==UserScript==
// @name         屏蔽知乎热门内容推荐
// @namespace    http://tampermonkey.net/
// @version      0.12
// @description  【已弃用】屏蔽知乎feed流的热门推荐以及来自话题推荐，代码简单一看就懂
// @author       LaiYao
// @match        https://www.zhihu.com/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    let lastItemCount = 0;
    const selectItems = () => document.querySelectorAll('.TopstoryItem');
    const doRemove = () => {
        const newItems = selectItems();
        if (newItems.length !== lastItemCount) {
            Array.from(newItems)
                .filter(a => a.innerText.indexOf('热门内容') > -1)
                .forEach(a => a.style.display='none');
            Array.from(newItems)
                .filter(b => b.innerText.indexOf('来自话题') > -1)
                .forEach(b => b.style.display='none');
            lastItemCount = newItems.length;
        }
    };
    const oldListener = window.onscroll;
    window.onscroll = () => {
        if (!!oldListener) oldListener();
        doRemove();
    };
    const oldOnload = window.onload;
    window.onload = () => {
        if (!!oldOnload) oldOnload();
        doRemove();
    };
})();