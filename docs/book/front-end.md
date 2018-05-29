# 写给自己，梳理一下我现在对前端知识结构的理解

今天想着做一件事情，给收藏夹分类。结果做着做着，发现这个任务的工作量超乎我的想象。有一些文章，可能很难界定说，它是哪一类的；而且自己还没有特别去梳理自己对前端知识结构的理解，使得在分类的时候层级也有些模糊。所以在这里梳理一下自己理解中的知识结构。

这既是一篇总结，也是一篇指南，有些地方我自己亲身经历可能丰富一点，就说的多一些；有些地方自己没什么实践，就少说话，简单提一提，免得贻笑大方。

还有一点，这份指南中，个人色彩很重。有些学习方法上的建议，我都是从自己的经历出发的，但肯定不适合所有人。比如我喜欢浅阅读，看很多东西，需要用到的时候，心里有个大概，然后再深入研究，用到项目中。但我也遇到过一些喜欢深阅读的同学，他们看到一个东西就喜欢深入学习，举一反三。认识自己的特点并且选择适合自己的方法非常重要，就像小马过河的故事一样。

## JavaScript

就语言本身，JavaScript值得深究的地方不多。很多同学在最开始入行的时候（就像我），可能根本不懂就已经开始开发了。虽说在开发中踩坑，在踩坑中理解也未尝不可，不过我现在觉得，一开始先了解一些很常用的语法，还是很重要的。

我对前端的JavaScript学习，列出了这样的结构：

 - 语法
 - 框架与类库
 - 设计模式
 - 函数式
 - 底层
 - 发展

接下来就各个层面进行阐述：

### 语法

关于语法，JavaScript中值得注意的大点，其实也不是特别多，大概就以下几方面是比较常用的：

 - 变量提升
 - this 指向
 - 深复制和继承的写法
 - 闭包
 - 高阶函数
 - 异步与事件模型

关于语法，现有的资料其实很多。从我自己的学习经历来看，我是先简单过一遍《JavaScript高级程序设计》，有一个大概的理解，另外准备一本《JavaScript权威指南》当字典（高程其实也是字典）。建议深入阅读[《You Don't Know JS》](https://github.com/getify/You-Dont-Know-JS)这一系列，写的真心非常好。

其他资料也推荐一些供大家选择：

 - [JavaScript秘密花园](http://bonsaiden.github.io/JavaScript-Garden/zh/)
 - [Mozilla 开发者网络](https://developer.mozilla.org/)

### 框架与类库

其实很多时候，能听到将jQuery称为框架的这种声音，我觉得是不妥的。常用的第三方包大概两种，框架（framework）和库（library）。我界定两者的标准是：框架会影响到你项目的目录结构、代码结构以及编程模型这些设计相关的东西，而库则仅仅是提供了某些或某类操作的简洁封装方便调用。框架中包含的概念，一般要比库复杂的多，所以我觉得jQuery是一个库，提供了关于DOM操作，Ajax请求等一系列常用操作的简洁封装，而算不上框架。

就我所知，现在比较常见的框架如下：

 - React
 - Angular 2
 - Angular 1
 - Ember
 - Polymer
 - Vue
 - Riot

有人还做了这样一张表格，将这些框架进行了对比：[Front-end Hyperpolyglot](http://jeffcarp.github.io/frontend-hyperpolyglot/)

其实还有rxjs / cycle.js这个纯粹的函数式的框架活跃着，ng2使用了rxjs，React也从中借鉴了思想（包括在redux中用rxjs处理异步Action），但纯粹用这一套的项目，应该还是demo多吧。

我对于框架学习的态度是：将一个真正用到项目中，了解一下其他框架的特点和主要思想（当然时间足够且不怕忘的话，多来几个也没问题，还是那句话，根据自己特点来）。其实哪怕框架过时了，思想也还是有价值的。其实我觉得现在就很像jQuery统治世界之前的样子。现在来看，最终谁会胜出还是个未知数。

然而对于很多同学来说，可能很难去在项目中学习一个框架：自学只能敲demo，项目不熟不敢用。确实，demo的复杂度不足以让你从工程的层次去学习框架，而这一点我的建议就是，借用公共的API进行开发。我推荐使用GitHub和豆瓣（并不是广告），其他文档全面稳定且复杂度足够的API也没有问题。我认为只要你开发了一个足够复杂的前端项目，就能切身体会到框架所带来的优缺点。（其实只要解除跨域限制，哪的API都可以用，方法就是使用代理软件，后面讲开发与调试的时候会具体说）

上面说的这些框架，更准确的来说，其实是专注于将表现和数据分离的框架。其实还有很多框架不在这一类，如针对游戏开发的Egret。（游戏这个领域我没有接触过，点到为止）

说到库的话，我觉得大概有两类：一类相对来说通用一些，如jQuery、lodash；另一类相对专用，如针对数据可视化的D3、Highcharts，针对3D图形的three.js，甚至比较简单的如针对时间处理的moment等等。整体来说，库的上手程度不高，比如jQuery，理解清楚被jQuery的$符包裹的对象和普通DOM的区别及其相互转化，剩下的应该就只有查文档了。

相关推荐：

 - [jQuery 技术内幕](https://book.douban.com/subject/25823709/)
 - [犀利开发:jQuery内核详解与实践](https://book.douban.com/subject/5063431/)
 - [UnderScore源码分析](http://www.w3cfuns.com/house/17398/note/class/id/bb6dc3cabae6651b94f69bbd562ff370.html)
 - [Backbone0.9.1源码分析分析系列](http://www.cnblogs.com/nuysoft/archive/2012/03/14/2395260.html)
 - [100 行代码实现的 JavaScript MVC 样式框架](http://www.oschina.net/translate/javascript-mvc-style-framework-in-less-than-lines)（翻译有点问题，原文的style我的理解是风格）
 - [只有20行Javascript代码！手把手教你写一个页面模板引擎](http://blog.jobbole.com/56689/)

### 设计模式

对设计模式的使用，应该是一种经验的体现。由于个人经验缺乏，我现在对设计模式用的很少，仅仅简单实践过像策略模式、装饰者模式这些。我认为设计模式应该是要用心去学习的一个点，也是提升能力的一个有效途径。

相关资料：

 - [JavaScript设计模式与开发实践](https://book.douban.com/subject/26382780/)
 - [常用的Javascript设计模式](http://web.jobbole.com/29454/)

### 函数式

前端的函数式编程，应该在近年来火起来的。其实在高级程序设计上，就对JavaScript的函数式编程有所涉及。函数式编程的起源要从λ演算说起，有兴趣可以查阅相关资料。就我目前的感觉来说，在JavaScript中应用函数式编程更像是一种高级技巧，这种技巧一般都会涉及到闭包和高阶函数，反正我觉得，真心好用。

举一个简单的例子：写一个`before`函数（`before(count, function)`），返回一个函数，调用不超过`count`次。 当`count`已经达到时，最后一个函数调用的结果将被记住并返回。

比如，我传入这样一个函数：

```js
function log() {
  console.log.apply(console, arguments)
  return arguments[0]
}
```

用`before`函数获得只能执行3次的log：

```js
var log3 = before(3, log)

log3(1)   // 1
log3(2)   // 2
log3(3)   // 3
log3(4)   // 什么都没有log
```

想一想，你会怎么实现这个`before`函数。

```js
  // Returns a function that will only be executed up to (including) the Nth call.
  _.before = function(times, func) {
    var memo;
    return function() {
      if (--times >= 0) {
        memo = func.apply(this, arguments);
      }
      if (times < 0) func = null;
      return memo;
    };
  };
```

还有一些非常常用的函数节流技巧（`throttle`、`debounce`）、封装一些原生函数（如`fetch`），都会用到这相关的技巧。在ES7中，提供了Decorators相关的语法，让你更方便的使用这些技巧。（这其实就是JavaScript中的装饰者模式实践）

 - [ES7 Decorator 装饰者模式](http://taobaofed.org/blog/2015/11/16/es7-decorator/)

许多框架在设计上借鉴了函数式的技巧，比较明显的就是Redux，包括在Redux的源码中，也遍布各种函数式的思维。rxjs更是将这种思维贯彻到了一个极致。我觉得将来rxjs包括cycle.js肯定会在框架中占据一席之地，目前来说，至少RxJava发展的还是挺好的。

推荐：

 - [编程语言的基石——Lambda calculus](http://liujiacai.net/blog/2014/10/12/lambda-calculus-introduction/)
 - [JS函数式编程指南](https://www.gitbook.com/book/llh911001/mostly-adequate-guide-chinese/details)
 - [延续性究竟是什么？](http://www.zcfy.cc/article/365)
 - [用 JavaScript 实现单步调试](http://www.zcfy.cc/article/363)

### 底层

JavaScript能有今天的发展跟V8是脱不了关系的。很多讲解JavaScript优化的文章，都会提到V8相关的实现。

不过我觉得，对于V8这一层面的东西，离前端还是有点远了。目前我在浏览器开发，没遇到过什么性能上的大问题，学习V8源码，也不算是核心痛点。推荐几篇相关文章：

 - [A tour of V8](http://jayconrod.com/tags/v8)
 - [V8常见去优化原因一览](http://alinode.aliyun.com/blog/25)

### 发展

其实很想吐槽一下，现在的JS，一年一个版本，太可怕了。

当然，确实提供很多非常好用的语法（糖），比如class、解构、箭头函数这些，我是挺喜欢用的。

另外一支很有势头的发展就是TypeScript，给JavaScript加入了强类型，使其更易于开发大型项目（接口的规范与更好的错误提示）。AngularJS 2已经全面拥抱TypeScript了，蚂蚁金服的Ant-Design也已经切换到了TypeScript，可见其提供的特性还是很有吸引力的。在微软推出了VS Code之后，TypeScript也有了官方的编辑器，值得一试。

在使用这些新特性的时候，一般都会用到类似babel这种转换工具。关于这类工具的介绍，会在下面讲开发与调试的时候提到。

## HTML & CSS

很多前端同学应该都是从这个地方入的坑吧。关于HTML和CSS的技巧，我觉得现在自己已经在某种程度上生疏了，毕竟很久没有自己写过了。

其实这个领域曾经带给我很多乐趣，黑科技在某种程度上讲要比JavaScript多很多，而且也是和浏览器兼容的斗争最紧张的地方。如果想了解一些黑科技的话，建议阅读[张鑫旭的博客](http://www.zhangxinxu.com/)，读下来肯定会很有收获。

下面是我觉得很有意思的几篇文章：

 - [小tips: 使用&#x3000;等空格实现最小成本中文对齐](http://www.zhangxinxu.com/wordpress/2015/01/tips-blank-character-chinese-align/)
 - [CSS3 pointer-events:none应用举例及扩展](http://www.zhangxinxu.com/wordpress/2011/12/css3-pointer-events-none-javascript/)
 - [CSS中的负边距](https://segmentfault.com/a/1190000005856540)
 - [CSS之BFC详解](http://www.html-js.com/article/1866)

学习CSS的话，推荐下面这些材料：

 - [精通CSS（第2版）](https://book.douban.com/subject/4736167/)
 - w3cplus[http://www.w3cplus.com/](http://www.w3cplus.com/)
 - 前端乱炖[http://www.html-js.com/](http://www.html-js.com/)

其他资料推荐：

 - [理解WebKit和Chromium](http://www.ituring.com.cn/minibook/705)

## 开发与调试

准备好了基础知识，让我们简单了解一下开发与调试相关的东西。在这一部分中，工具发挥着很大的作用。

- 列一个大纲：
  - 规范
  - 构建
  - 调试
  - 协同
  - 测试
  - 性能

### 规范

没有规矩不成方圆，写代码的时候团队肯定要有一套规范。也有许多团队将他们的规范拿了出来，比如：

 - [alloyteam代码规范](http://alloyteam.github.io/CodeGuide/)
 - [airbnb代码规范](https://github.com/airbnb/javascript)
 - [前端代码规范 及 最佳实践](http://blog.jobbole.com/79075/)

其他团队的规范未必适合自己，只要团队成员达成共识，就是好的规范。

在代码commit之前进行规范的检测是一个比较合适的时机，npm提供了一个叫做`pre-commit`的包，结合`eslint-config-airbnb`，可以搭建一套用于质量保证的东西出来。

相关资料：

 - [eslint-config-airbnb](https://www.npmjs.com/package/eslint-config-airbnb)
 - [pre-commit](https://www.npmjs.com/package/pre-commit)

### 构建

构建一般是使用webpack来进行，依靠各种强大的loader，可以完成一系列功能。强烈建议结合`npm script`管理项目的命令。

相关资料：

 - [React Webpack 小书](http://fakefish.github.io/react-webpack-cookbook/)
 - [webpack使用优化](http://www.alloyteam.com/2016/01/webpack-use-optimization/)
 - [如何 10 倍提高你的 Webpack 构建效率](http://eternalsky.me/ru-he-10-bei-ti-gao-ni-de-webpack-gou-jian-xiao-lu/)

### 调试

我最常用的工具应该就是Chrome Dev Tools了：

 - [Chrome DevTools 官方文档](https://developer.chrome.com/devtools)
 - [Chrome开发者工具系列](http://www.cnblogs.com/constantince/category/712675.html)
 - [chrome 控制台使用指南](http://frontenddev.org/column/chrome-development-tools-using-guide/)
 - [Chrome开发者工具之JavaScript内存分析](http://www.open-open.com/lib/view/open1421734578984.html)
 - [一探前端开发中的JS调试技巧](http://seejs.me/2016/03/27/jsdebugger/)

另外就是前面提到过的代理工具，Chrome插件Proxy SwitchyOmega配合fiddler / charles，进行线上调试。如果代理的自定义需求比较高，工具的正则满足不了，可以尝试自己写一个nodejs程序，用`http-proxy`这个包来将资源代理到本地。

 - [如何使用Fiddler调试线上JS代码](http://www.cnblogs.com/RockLi/p/3511132.html)
 - [在线调试利器Fiddler AutoResponse](http://www.cnblogs.com/peak-weng/archive/2012/01/19/2325855.html)

### 协同

推荐使用git，毕竟GitHub对于开发者已经如同简历、名片一般。

 - [廖雪峰的Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
 - [Pro Git 简体中文版](http://iissnan.com/progit/)
 - [基于git的源代码管理模型——git flow](http://www.ituring.com.cn/article/56870)
 - [我的提交信息规范](http://yanhaijing.com/git/2016/02/17/my-commit-message/)
 - [多 SSH Key 管理技巧与 Git 多账户登录问题](http://www.barretlee.com/blog/2016/03/09/config-in-ssh-after-troubling-git-connection/)
 - [git子模块](https://yuguo.us/weblog/git-submodule/)

### 测试

测试是对代码质量的保证，不过说来惭愧，我就没有比较好的测试习惯（这也是我打算培养的一种习惯）。

我对测试重要性的认识来源于在OJ上刷算法题，很多时候抛出一个WA（Wrong Answer）就什么都没有了，一时间就不知道从何去debug。后来在LeetCode上刷题的时候，至少可以看到报错的测试用例，能看到预期的输出，这样思路很快就下来了。有一个同学跟我说，他在LeetCode上做题时，本地测试的过程中，就顺便把测试给写了，自己的测试跑过了再提交，有问题再完善本地测试。如此一个流程下来，不仅加深了对题目的理解，也养成了测试的习惯，思考问题的时候考虑的也会更全面一些（我也想这么试试）。

测试主要针对的是逻辑，在前端对UI测试个人认为是一件很麻烦的事情。之前见过ThoughtWorks的一个工具，将页面在各个浏览器中截图，然后进行对比，看看有没有特别大的问题。虽然也是一种可行的方案，但当页面中有大量的按钮可以点，大量的交互操作去处理，截图来对UI进行测试感觉会比较复杂。

而对逻辑进行测试，工具就相对成熟一些，一般分为以下三类（附上推荐）：

 - 测试框架：[mocha](http://mochajs.org/)
 - 断言库：[chai](http://chaijs.com/)
 - mock库：[sinon](http://sinonjs.org/)

对于测试我也是新手，所以推荐阮一峰老师的入门文章：[测试框架 Mocha 实例教程](http://www.ruanyifeng.com/blog/2015/12/a-mocha-tutorial-of-examples.html)。同样，在很多成熟的Github项目上，你都能看到一个叫test的文件夹，在这里面可以看到项目开发人员所写的测试，学习测试的写法。

## 工程问题

### 性能

前端性能问题，很难在写的时候就全都避免，一般都是在开发完成的测试阶段遇到问题后逐步排查的，总会多少经历一个迭代的过程。

影响前端性能的问题有很多，比如网络速度太慢会影响首屏时间；代码的一些写法也会影响到浏览器的渲染；还有一点我觉得很值得注意的就是内存泄漏。相关的议题都有很多工具去处理，如果前面Chrome开发者工具部分有好好研究的话，现在对性能问题应该也有一些心得了。

关于加载：

 - [大公司里怎样开发和部署前端代码？](https://www.zhihu.com/question/20790576)
 - [bigpipe性能优化](http://www.alloyteam.com/2015/03/bigpipe%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96/)

关于渲染：

 - [渲染性能](https://github.com/sundway/blog/issues/2)

关于内存泄漏：

 - [js内存泄漏常见的四种情况](https://segmentfault.com/a/1190000004896090)

其他资料推荐：

 - [前端优化不完全指南](https://aotu.io/notes/2016/03/16/optimization/)
 - [JavaScript 性能优化杀手](http://dev.zm1v1.com/2015/08/19/javascript-optimization-killers/)
 - [编写高性能JavaScript](http://www.alloyteam.com/2012/11/performance-writing-efficient-javascript/)
 - [了解 JavaScript 应用程序中的内存泄漏](http://www.ibm.com/developerworks/cn/web/wa-jsmemory/)
 - [搞定JavaScript内存泄漏](https://boke.io/gao-ding-nei-cun-xie-lou/)

### 安全

前端代码没有秘密，毕竟就算混淆也是看的到的。但是，一些安全上的失误，还是会造成不小的影响。可以看看下面这些事件：

 - [一个 JSON 跨域获得数据漏洞的分析](http://ju.outofmemory.cn/entry/62159)
 - [事件还原：一封QQ恶意邮件，导致Apple ID密码丢失](http://www.freebuf.com/vuls/85053.html)
 - [关于恶意说说自动在QQ空间转发的机制](https://zsy.blog.ustc.edu.cn/archives/133)
 - [前端XSS高阶玩法](http://www.alloyteam.com/2014/11/qian-duan-xss-gao-jie-wan-fa/)

对于安全的具体学习，推荐大家阅读：

 - [Web前端黑客技术揭秘](https://book.douban.com/subject/20451827/)
 - [白帽子讲Web安全](https://book.douban.com/subject/10546925/)

### 监控

一般来说，测试没有错不代表上线没有错。尤其是现在可以接入网络的设备越来越多，加上本来就很多的浏览器，测试环境几乎是不可能完美模拟线上的环境的。因此，对错误进行监控就非常重要。

关于前端监控，目前也没有特别完善的解决方案，给出两篇文章供大家参考：

 - [前端代码异常日志收集与监控](http://www.cnblogs.com/hustskyking/p/fe-monitor.html)
 - [构建web前端异常监控系统–FdSafe](http://www.aliued.cn/2012/10/27/%E6%9E%84%E5%BB%BAweb%E5%89%8D%E7%AB%AF%E5%BC%82%E5%B8%B8%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F-fdsafe.html)

## 业务场景

### PC端

传统的PC端场景，如果不考虑老式浏览器的话，其实是很美好的。目前大部分PC端的业务，如果是针对普通用户的话，一般会兼容到IE8。有特殊需要的（如政府网站），会要求兼容到IE7（甚至更低）。如果是针对企业用户或者内部用户的话，其实就可以开开心心的不考虑兼容了。相信很多同学都是从PC端业务开始的，应该都比较熟悉，就不多说了。

为了方便大家的调试，这里我分享一下微软良心出品：

- [微软各版本IE虚拟机](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/)

### 移动端

关于移动端的开发，会涉及很多新的问题，可以先看看下面这篇文章了解一下大概的特点：

 - [无线Web开发者指南](https://github.com/semious/guide/blob/master/mobile_exp.md)

其实最实用的就是，主要考虑webkit、rem和flex都可以用。这个我认为是和PC端最大的区别。

移动端开发现在也已经有了很长一段时间，也有许多团队分享了相关的经验：

 - [移动web问题小结](http://www.alloyteam.com/2015/06/yi-dong-web-wen-ti-xiao-jie/)
 - [手机淘宝的flexible设计与实现](http://www.html-js.com/article/2402)
 - [使用Flexible实现手淘H5页面的终端适配](https://github.com/amfe/article/issues/17)

移动端和PC另一个很大的不同就是调试，真机调试是必不可少的环节，也有许多相关的解决方案：

 - [移动开发真机调试](http://www.cnblogs.com/constantince/p/4711098.html)
 - [微信调试工具](http://blog.qqbrowser.cc/)

### 细分场景

针对终端对业务场景进行分类仅仅是一种方法，其他时候，还有许多细节的场景需要我们去分析，仅就我个人经验谈一下我所知的几种场景：

#### 纯静态展示页面

建议使用jQuery（移动端Zepto）进行开发，主要任务是切图，一般公司首页这种比较多。

#### 企业后台

用React做这类项目我认为是非常合适的。组件好分，逻辑清楚，样式、兼容性也不用太在意，主要靠UI框架。

#### H5动画（广告）

有一个H5动画惊艳了我，让我见到了这一类项目的潜力。[罗斯·决不凋谢](http://drose6.adidasevent.com/)，请在移动端（或模拟环境）打开。

看到这个项目之后，从代码注释中发现了作者并大概看了一下作者的一系列项目，感觉这个方向也是自有一套东西的（对于只关注于业务开发的我，像发现了新大陆一样）。作者是[@shrekshrek](https://github.com/shrekshrek)，有兴趣的同学可以关注一下。

相关文章推荐：

 - [前端动画原理与实现](http://matrix.h5jun.com/slide/show?id=117#/)
 - [缓动函数速查表](http://easings.net/zh-cn)
 - [JavaScript基于时间的动画算法](https://github.com/livoras/blog/issues/8)

#### 游戏

对于这个领域，我就更是陌生了。如果有同学愿意赐教，感激不尽。

#### 3D场景

WebGL给了浏览器3D的能力，Three.js则对相关的API进行了封装。这相关的业务可能会出现在游戏中，也可能会出现在一些展示性质的页面上。不过目前主要的项目中，WebGL相关的技术还没有大的应用场景。也许将来显卡性能和浏览器支持水平发展到了足够的高度，像Unreal一样的引擎，也许也会出现在浏览器之中。

当然实现3D也可能不需要JavaScript参与，CSS 3D现在应用的也很多。常见全景图展示效果，为了减小复杂度，经常会采用CSS来创建3D场景。

相关资料推荐：

 - [Three.js入门指南](http://www.ituring.com.cn/minibook/792)
 - [WebGL教程系列](https://www.script-tutorials.com/?s=WebGL+With+Three.js)
 - [打造H5里的“3D全景漫游”秘籍](https://isux.tencent.com/3d.html)
 <!-- - [细数html5几种360度全景展示方法](http://pan.baidu.com/s/1jIbHGv8) -->

## 面试

其实我觉得写这一部分是超出我能力的，毕竟自己没有什么经验，而面试这件事，无论是对面试官还是对应试者其实都是意见相当难的事情。下面所言仅仅是我自己的一些体会，希望抛砖引玉，换来各位前辈多多指教。

面试这件事是围绕人来的，主要的因素也在人。听过一句话，大意是：面试就是在寻找将来的同事。我认为，面试就是对自己的表达，需要一种表达的能力在里面，会表达的人，总是会占据很大的优势。

面试是需要准备的，我认为，面试的积累体现在三方面，也是我接下来希望阐述的三方面：

 - 试题的积累
 - 项目的积累
 - 思考的积累

### 试题的积累

试题的积累是肯定要做的，因为很多时候，在初筛和一面这种基数很大的情况时，直接用题目来筛掉一波人是很有效率的行为。前端的试题，网上能找到很多，有一些很套路，也有一些很个性。不过考察JavaScript，肯定会问一些闭包、this相关的问题；考察CSS，居中的上镜率就很高；考察兼容，肯定离不开各种奇葩浏览器的hack。有一些小众的东西，可能你没有在项目里面用过，但是面试官如果问到了，且在常见问题中，那你就吃亏了。所以，准备是肯定要做的。

相关资源推荐：

 - [前端开发面试题](https://github.com/markyun/My-blog/tree/master/Front-end-Developer-Questions)

### 项目的积累

面试中另一个常见问题就是，你做过什么项目。我觉得针对这个问题的话，重点要体现这个项目的特点（展示你对需求的理解能力和分析能力）以及你在这个项目中解决了什么问题（展示你解决问题的能力）。项目应该具有一定的复杂度，如果你在上家公司主要是切图的话，要么就谈谈你对CSS相关的积累，或者直接就谈一些自己做的有一定复杂度的项目（还能展示你自学的能力和动力）。按照这个思路来的话，应该问题不大。

### 思考的积累

我觉得着应该是开发者的一种修养，也是开发者核心价值的一种体现。思考框架背后的东西，思考设计背后的东西，以及，广泛的阅读。

相关书籍推荐：

 - [人月神话](https://book.douban.com/subject/2230248/)
 - [数学之美 （第二版）](https://book.douban.com/subject/26163454/)
 - [黑客与画家](https://book.douban.com/subject/6021440/)

其他资源推荐：

 - [如何重构一个大型历史项目——百度经验改版总结](http://yanhaijing.com/program/2016/04/14/how-to-reconstruct-a-large-historical-project/)

## 其他

这一部分，会提及一些和前端工作相关的，我认为值得一提的东西。然而毕竟是其他领域的东西，难免会因个人眼界而言辞不当，希望各位前辈多多指教。

### 提问

一般在技术群里面，不懂提问浪费时间的人真是太多了。希望能够静下心来阅读张鑫旭的[如何提问才能进阶成为前端大神？](http://www.zhangxinxu.com/wordpress/2015/05/how-to-ask-web-front-question/)。节省别人的时间也是节省自己的时间。

其实很多时候，大家只要把最小可复现bug的线上demo做出来，说不定就已经不需要提问了。

### 获取学习资源

开发人员的时间非常宝贵（因为大家都很忙）。所以，阅读文章一定要精，多了根本看不过来。

我现在真正还在关注的资源，应该就只有[JavaScript Weekly](http://javascriptweekly.com/)和[奇舞周刊](http://old.75team.com/weekly/)了。对于我来说，已经足够了。

### 数据结构与算法

对于数据结构与算法这部分，我曾经专门写过一篇文章来讨论这个问题，欢迎拍砖：

 - [为什么我认为数据结构与算法对前端开发很重要？](https://github.com/LeuisKen/leuisken.github.io/issues/2)

做题推荐：

 - [LeetCode](https://leetcode.com/)

阅读推荐：

 - [算法导论](https://book.douban.com/subject/20432061/)
 - [算法设计与分析基础](https://book.douban.com/subject/26337727/)
 - [程序员代码面试指南：IT名企算法与数据结构题目最优解](https://book.douban.com/subject/26638586/)

算导没有读过，不过毕竟经典。后面两本我还没有读完，感觉都很不错。

### HTTP

HTTP2的发展可能会为前端带来很多机会，对这方面感兴趣的同学，可以去看看[Jerry Qu的小站](https://imququ.com/)。

相关资料推荐：

 - [HTTP权威指南](https://book.douban.com/subject/10746113/)
 - [计算机网络（第6版）](https://book.douban.com/subject/26176870/)（我的大学教材）

### 后端和数据库

建议前端开发至少了解一门后端框架，至少了解网站是怎么回事，有一个整体的把握。推荐一下之前我写的[WEB开发新人指南](https://segmentfault.com/a/1190000003063481)。

我自己的经历，是先后学习了ThinkPHP和express这两个后端开发框架，写了一些简单的东西。私以为比较重要的点如下：

 - cookie和session
 - 路由控制
 - 权限控制
 - 如何去建表

Node.js的使用现在也已经是前端的必备技能了（注意是使用）。主要就是使用npm、require的路径规则、能够解决报错信息这些。

建议使用nvm用来做Node版本控制，Windows下需要单独处理`node-gyp`的环境问题，详见：[https://github.com/TooTallNate/node-gyp#installation](https://github.com/TooTallNate/node-gyp#installation)。另外，强烈不建议在Windows下进行Node开发。

推荐阅读：

 - [Head First PHP & MySQL](https://book.douban.com/subject/6011680/)
 - [七天学会NodeJS](http://nqdeng.github.io/7-days-nodejs/)
 - [Node.js 包教不包会](https://github.com/alsotang/node-lessons)
 - [nodejs stream 手册](https://github.com/jabez128/stream-handbook)

### Shell

使用终端也是一项必备技能。首先如果你使用git的话，肯定会用到；此外仅仅善用一些基本技巧，就能大大提高你的开发效率。

使用是最好的学习方法，首先，把Windows弃了吧（或者丢到虚拟机里面）。

## 总结与前瞻

可能以后很多新的东西会进入我们的视野，比如：

 - [Google的Progressive Web App](https://developers.google.com/web/fundamentals/getting-started/your-first-progressive-web-app/?hl=zh-cn)

Babel等一系列JS的工具，也让AST（抽象语法树）进入了前端的视野，并且开始了应用：

 - [抽象语法树在 JavaScript 中的应用](http://tech.meituan.com/abstract-syntax-tree.html)
 - [通过开发 Babel 插件理解抽象语法树（AST）](http://www.zcfy.cc/article/347)

WebRTC也已经开始被浏览器支持了，即时通讯的开发也许会变的更加简单。

框架之战，也没有出现明显的胜利者。

等待VR设备普及起来，我们也许也会在上面写代码？毕竟现在JS跑的地方，已经到嵌入式设备了。

机会和挑战是并存的，而新的东西投入应用，也是一个渐进的过程。放眼未来，还要脚踏实地，能够切实用起来的东西，还是最重要的。

#个人收藏夹中的链接

本文件为个人浏览器收藏夹内容的整理，包含所接触的各种开发（前端为主）相关的资源

##前端资源
 - [Sublime Text 手工汉化和插件开发、提交方法教程（一）——手工汉化](http://blog.csdn.net/theforever/article/details/8962727)
 - [有意思的腾讯web前端在线试题(附上通关攻略)](http://www.w3cways.com/394.html)
 - [手机淘宝的flexible设计与实现](http://www.html-js.com/article/2402)
 - [持续集成工具的选择](http://www.iteye.com/topic/482658)
 - [【Sass中级】使用Sass和Compass制作雪碧图](http://www.w3cplus.com/preprocessor/intermediate/spriting-with-sass-and-compass.html)
 - [jasmine行为驱动,测试先行](http://blog.fens.me/nodejs-jasmine-bdd/)
 - [Git查看、删除、重命名远程分支和tag](http://zengrong.net/post/1746.htm)
 - [一个中国地图的SVG，可以带参数](http://www.cnblogs.com/LoveOrHate/p/4438081.html)
 - [圣杯布局](http://alistapart.com/article/holygrail)
 - [CuteSlider](http://www.cuteslider.com/)
 - [小tips: 使用&#x3000;等空格实现最小成本中文对齐](http://www.zhangxinxu.com/wordpress/2015/01/tips-blank-character-chinese-align/)
 - [八种创建等高列布局](http://www.w3cplus.com/css/creaet-equal-height-columns)
 - [Nazo](http://cafebabe.cc/nazo/)
 - [segmentfault-d-day](http://segmentfault.com/t/segmentfault-d-day/info)
 - [Javascript模块化编程（三）：require.js的用法](http://www.ruanyifeng.com/blog/2012/11/require_js.html)
 - [前端开发人员都在关注的 GitHub 资源](http://www.yyyweb.com/3427.html)
 - [webkit webApp 开发技术要点总结](http://www.cnblogs.com/pifoo/archive/2011/05/28/webkit-webapp.html)
 - [移动开发真机调试](http://www.cnblogs.com/constantince/p/4711098.html)
 - [前端资源分享：GitHub免费编程中文书籍](http://html5.9tech.cn/news/2014/0117/39658.html)
 - [手机QQ浏览器调试解决方案](http://bbs.mb.qq.com/thread-227056-1-1.html)
 - [Shadow DOM：基础](http://www.ituring.com.cn/article/177461)
 - [前端书签](https://github.com/dypsilon/frontend-dev-bookmarks)
 - [微软各版本IE虚拟机](https://dev.windows.com/zh-cn/microsoft-edge/tools/vms/linux/)
 - [关于恶意说说自动在QQ空间转发的机制](https://zsy.blog.ustc.edu.cn/archives/133)
 - [WebGL教程系列](https://www.script-tutorials.com/?s=WebGL+With+Three.js)
 - [使用node-webkit构建桌面应用程序（一）](http://www.infoq.com/cn/articles/using-node-webkit-to-build-desktop-applications-part1)
 - [React 在 Coding WebIDE 中的应用实践](https://blog.coding.net/blog/React-practice-Coding-WebIDE)
 - [D3.js](http://www.ourd3js.com/wordpress/?p=127)
 - [React 中文索引](http://nav.react-china.org/)
 - [JavaScript中变量提升------Hoisting](http://www.cnblogs.com/damonlan/archive/2012/07/01/2553425.html)
 - [腾讯大燕网前端规范](http://bj.jjj.qq.com/zt/guifan/)
 - [理解Javascript的闭包](http://coolshell.cn/articles/6731.html)
 - [搞定immutable.js](http://boke.io/immutable-js/)
 - [100 行代码实现的 JavaScript MVC 样式框架](http://www.oschina.net/translate/javascript-mvc-style-framework-in-less-than-lines)
 - [只有20行Javascript代码！手把手教你写一个页面模板引擎](http://blog.jobbole.com/56689/)
 - [[原创]Backbone0.9.1源码分析分析系列（停止更新）](http://www.cnblogs.com/nuysoft/archive/2012/03/14/2395260.html)
 - [Angularjs 源码分析1](http://www.angularjs.cn/A0Ad)
 - [CSS实现垂直居中的5种方法](https://www.qianduan.net/css-to-achieve-the-vertical-center-of-the-five-kinds-of-methods/)
 - [CSS之BFC详解](http://www.html-js.com/article/1866)
 - [Backbone.js 源码阅读](https://segmentfault.com/a/1190000002416438)

 - [Redux 中文文档](https://camsong.github.io/redux-in-chinese/index.html)
 - [React Router](http://react-guide.github.io/react-router-cn/docs/Introduction.html)
 - [Full-Stack Redux Tutorial](http://teropa.info/blog/2015/09/10/full-stack-redux-tutorial.html)
 - [Vue.js](http://cn.vuejs.org/guide/reactivity.html)
 - [CSS3 pointer-events:none应用举例及扩展](http://www.zhangxinxu.com/wordpress/2011/12/css3-pointer-events-none-javascript/)
 - [深度剖析：如何实现一个 Virtual DOM 算法](https://github.com/livoras/blog/issues/13)
 - [用Promise组织程序](http://www.w3ctech.com/topic/721)

 - [“函数是一等公民”背后的含义](http://blog.leapoahead.com/2015/09/19/function-as-first-class-citizen/)
 - [微信、手Q、Qzone之x5内核inspect调试解决方案](http://bbs.mb.qq.com/thread-243399-1-1.html?pid=313743&fid=93)
 - [charles破解 sn 注册码](http://www.gfzj.us/2014/12/20/charlse-sn-download.html)
 - [如何百倍加速 Lo-Dash？引入惰性计算](http://blog.csdn.net/justjavac/article/details/50323537)
 - [Captain Obvious on JavaScript](https://github.com/raganwald-deprecated/homoiconic/blob/master/2012/01/captain-obvious-on-javascript.md)
 - [解读redux工作原理](https://segmentfault.com/a/1190000004236064)
 - [Redux系列](http://www.cnblogs.com/chyingp/p/)
 - [深入到源码：解读 redux 的设计思路与用法](http://div.io/topic/1309)
 - [CSS文件动态加载（续）—— 残酷的真相](http://www.cnblogs.com/chyingp/archive/2013/03/03/how-to-judge-if-stylesheet-loaded-successfully.html)
 - [Nodejs 制作命令行工具](http://jslite.io/2015/06/19/Nodejs-%E5%88%B6%E4%BD%9C%E5%91%BD%E4%BB%A4%E8%A1%8C%E5%B7%A5%E5%85%B7/)
 - [happypoulp/redux-tutorial](https://github.com/happypoulp/redux-tutorial)
 - [[译]看这些文章，足够你学好redux](https://segmentfault.com/a/1190000004212752)
 - [前端编程提高之旅（十二）----position置入值应用](http://blog.csdn.net/yingyiledi/article/details/41120189)
 - [reactjs/react-redux](https://github.com/reactjs/react-redux)
 - [ggordan/react-infinite-grid](https://github.com/ggordan/react-infinite-grid)
 - [Hello Sea.js](http://island205.github.io/HelloSea.js/index.html)
 - [jsPerf — JavaScript performance playground](http://jsperf.com/)
 - [前端工程师需要明白的「浏览器渲染」](http://www.jianshu.com/p/e305ace24ddf)
 - [electron](http://electron.atom.io/)
 - [why-do-browsers-match-css-selectors-from-right-to-left](http://stackoverflow.com/questions/5797014/why-do-browsers-match-css-selectors-from-right-to-left/5813672#5813672)
 - [夜深人静写算法（1）：搜索入门](http://blog.jobbole.com/96312/)
 - [七步从AngularJS菜鸟到专家（4和5）：指令和表达式](http://blog.jobbole.com/50022/)
 - [为现代JavaScript开发做好准备](http://blog.jobbole.com/66135/)
 - [前端组件化开发实践](http://web.jobbole.com/82689/)
 - [2016年你应该学习的语言和框架](http://wx.h5.vc/post/translations/2015-12-14)
 - [Javascript Cheat Sheet](http://overapi.com/javascript)
 - [React 入门教程](https://www.gitbook.com/book/hulufei/react-tutorial/details)
 - [[Javascript] ES6 Generator基礎](http://huli.logdown.com/posts/292331-javascript-es6-generator-foundation)
 - [Web动画：学习使用API](http://www.w3cplus.com/animation/web-animations-learning-to-love-the-api.html)
 - [前端知识普及之页面加载](https://segmentfault.com/a/1190000004466407)
 - [[Javascript] Promise, generator, async與ES6](http://huli.logdown.com/posts/292655-javascript-promise-generator-async-es6)0
 - [DotHide/angular2-quickstart](https://github.com/DotHide/angular2-quickstart)
 - [大型 JavaScript 应用架构中的模式](http://nuysoft.com/2013/08/13/large-scale-javascript/)
 - [使用JavaScript进行基本图形操作与处理](http://www.ituring.com.cn/article/121428)
 - [cycle.js](http://cycle.js.org/)
 - [Why I No Longer Use MVC Frameworks](http://www.infoq.com/articles/no-more-mvc-frameworks)

##后端资源
 - [Node.js实现PDF文件转HTML](http://blog.yourtion.com/nodejs-convert-pdf-to-html.html)
 - [ThinkPHP CURD操作](http://doc.thinkphp.cn/manual/curd.html)
 - [Python Web](http://www.cnblogs.com/game-over/tag/python%20web/)
 - [跟我一起Django](http://www.cnblogs.com/ganiks/p/django-install-and-init.html)
 - [[Nodejs]学习笔记五：二进制操作（Buffer）](http://www.mozlite.com/nodejs-buffer)
 - [REST 架构该怎么生动地理解？](http://www.zhihu.com/question/27785028/answer/48096396)
 - [wordpress教程](http://www.ashuwp.com/level/simple)
 - [正则表达式30分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm)

## 其他文摘
 - [Go语言文档](http://docscn.studygolang.com/doc/)
 - [白话经典算法系列](http://www.cnblogs.com/morewindows/category/314533.html)
 - [Vim Cheat Sheet](http://vim.rtorr.com/lang/zh_cn/)
 - [Nginx开发从入门到精通](http://tengine.taobao.org/book/)
 - [Linux入门教程](http://c.biancheng.net/cpp/linux/)
 - [Shell教程](http://c.biancheng.net/cpp/view/6994.html)
 - [跟我一起写 Makefile](http://blog.csdn.net/haoel/article/details/2886)
 - [麻省理工（MIT）牛人解说数学体系](http://blog.jobbole.com/94591/#comment-154391)
 - [微信调试工具](http://blog.qqbrowser.cc/)
 - [语义化版本 2.0.0](http://semver.org/lang/zh-CN/)
 - [DECO](https://www.decosoftware.com/)
 - [Data Structures & Algorithms](http://www.cnblogs.com/yangecnu/category/548373.html)
 -

##技术博客
 - [Xiaoho](http://xiaoho.com/)
 - [SaltTiger](http://www.salttiger.com/)
 - [玉伯的github](https://github.com/lifesinger/lifesinger.github.com/issues?q=is%3Aissue+is%3Aopen)
 - [以不变应万变](http://www.blogjava.net/coffee/archive/2007/11/05/158371.html)
 - [Do la a mo](http://amoamo.github.io/)
 - [张鑫旭](http://www.zhangxinxu.com/)
 - [汤姆大叔](http://www.cnblogs.com/TomXu/)
 - [winter的博客](http://winter-cn.cnblogs.com/)
 - [腾讯ISUX](http://isux.tencent.com/)
 - [Sneezry](https://sneezry.com/)
 - [校长阿四](http://www.cnblogs.com/xiaozhanga4/category/338265.html)
 - [咀嚼之味](http://jerryzou.com/)
 - [Jayce's Blog](http://blog.liqiang.me/)
 - [yusiyuan's blog](http://yusiyuan.top/)
 - [老D](http://laod.cn/)
 - [OKLAI'S BLOG](http://oklai.name/)
 - [TGideas](http://tgideas.qq.com/)
 - [TID](http://tid.tenpay.com/)
 - [Airen的博客](http://www.w3cplus.com/blogs/airen)
 - [西风微雨](http://www.lightrains.org/)
 - [PHODAL](https://www.phodal.com/)
 - [Laker](http://laker.me/blog/)
 - [nuysoft](http://www.cnblogs.com/nuysoft/)
 - [小撸](http://www.60sky.com/)
 - [淘宝前端团队](http://taobaofed.org/)
 - [沫鱼的前端世界](http://www.cnblogs.com/mofish/)
 - [efe](http://efe.baidu.com/)
 - [美团点评技术团队](http://tech.meituan.com/)

##常用网站
 - [博客园](http://www.cnblogs.com/)
 - [WebRTC中文社区](http://www.webrtcbbs.com/forum.php?mod=forumdisplay&fid=43)
 - [IBM文档库](http://www.ibm.com/developerworks/cn/topics/)
 - [九章算法](http://www.jiuzhang.com/)
 - [ITBooks 分享IT方面的电子书](http://books.iteblog.com/)
 - [龙哥盟 - 计算机电子书](http://it-ebooks.flygon.org/categories)
 - [Ubuntu 中文 Wiki](http://wiki.ubuntu.org.cn/%E9%A6%96%E9%A1%B5)
 - [正则表达式解析](http://regexper.com/)
 - [Highcharts中文网](http://www.hcharts.cn/index.php)
 - [css3pie](http://css3pie.com/)
 - [json-generator](http://beta.json-generator.com/)
 - [egghead.io](https://egghead.io/)

##WEB工具推荐-By Vizards
 - [SM.MS - https图床](https://sm.ms/)
 - [PageSpeed Insights - Google Developers](https://developers.google.com/speed/pagespeed/insights/)
 - [RunJS - 在线编辑、展示、分享、交流你的 JavaScript 代码](http://runjs.cn/)
 - [TinyPNG - 在线压缩PNG](https://tinypng.com/)
 - [沃通免费SSL证书申请](https://buy.wosign.com/free/?lan=cn#apply)
 - [思威贝空间 - 日本国东京都渋谷区直连机房，全面功能支持](http://member.sivbe.net)