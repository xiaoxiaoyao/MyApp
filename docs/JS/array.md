# JavaScript学习笔记：数组的push()、pop()、shift()和unshift()方法

- push()方法可以在数组的末属添加一个或多个元素
- shift()方法把数组中的第一个元素删除
- unshift()方法可以在数组的前端添加一个或多个元素
- pop()方法把数组中的最后一个元素删除

## JavaScript实现类似栈和队列的行为

了解这几种方法之后，我们就可以将它们结合起来，轻松的实现类似栈和队列的行为。

### 实现类似栈的行为

将push()和pop()结合在一起，我们就可以实现类似栈的行为。

### 实现类似队列的行为

将shift()和push()方法结合在一起，可以像使用队列一样使用数组。即在数组的后端添加项，从数组的前端移除项。

除此之外，还可以同时使用unshift()和pop()方法，从相反的方向来模拟队列，即在数组的前端添加项，从数组的后端移除项。

## push()方法和unshift()方法的性能测试

> 以下这部分内容来自于《JavaScript学习：JavaScript的数组实现队列与堆栈的方法》一文。

Array的push()与unshift()方法都能给当前数组添加元素，不同的是，push()是在末尾添加，而unshift()则是在开头添加，从原理就可以知道，unshift()的效率是较低的。原因是，它每添加一个元素，都要把现有元素往下移一个位置。但到底效率差异有多大呢?下面来简单测试一下。

```javascript
/*
关于代码中"var s=+newDate();"的技巧说明
解释如下:=+这个运算符是不存在的;
+相当于.valueOf();
+new Date()相当于new Date().valueOf()
//4个结果一样返回当前时间的毫秒数
  alert(+new Date());
  alert(+new Date);
  var s=new Date();
  alert(s.valueOf());
  alert(s.getTime());
*/
var arr = [ ];
var startTime = +new Date(); //+new Date()相当于new Date().valueOf()，返回当前时间的毫秒数
// push性能测试 
for (var i = 0; i < 100000; i++) { 
　　arr.push(i); 
}
var endTime = +new Date();
console.log("调用push方法往数组中添加100000个元素耗时"+(endTime-startTime)+"毫秒"); 

startTime = +new Date(); 
arr = [ ]; 
// unshift性能测试 
for (var i = 0; i < 100000; i++) { 
　　arr.unshift(i); 
}
endTime = +new Date();
console.log("调用unshift法往数组中添加100000个元素耗时"+(endTime-startTime)+"毫秒"); 
```

这段代码分别执行了100000次push()和unshift()操作，在chrome浏览器运行一次，得到的结果如下图所示：

调用push方法往数组中添加100000个元素耗时7毫秒

调用unshift法往数组中添加100000个元素耗时875毫秒

可见，unshift()比push()要慢差不多100倍!因此，平时还是要慎用unshift()，特别是对大数组。那如果一定要达到unshift()的效果，可以借助于Array的reverse()方法，Array的reverse()的方法能够把一个数组反转。先把要放进数组的元素用push()添加，再执行一次reverse()，就达到了unshift()的效果。