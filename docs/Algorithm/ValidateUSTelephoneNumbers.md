# 问题：验证输入的字符串是否符合美国电话号码规则

[题目链接](https://www.freecodecamp.cn/challenges/validate-us-telephone-numbers#?solution=%0A%0A%0A%0AtelephoneCheck(%22555-555-5555%22)%3B%0A)

[links:Validate US Telephone Numbers](https://www.freecodecamp.org/challenges/validate-us-telephone-numbers)

```js
function telephoneCheck(str) {
    // TODO：验证输入的字符串是否符合美国电话号码规则
  return true;
}

telephoneCheck("555-555-5555");
```

首先想到，电话号码嘛，正则表达式匹配纯数字，直接`\d{10}`连续7位数的电话号码，但是，看一下测试用例：

```js
var test = require('tape').test;
test('equivalence', function(telephoneCheck) {
    t.equal("555-555-5555", true, '美国电话号码');
    t.equal("(555)555-5555", true, '美国电话号码');
    t.equal("(555) 555-5555", true, '美国电话号码');
    t.equal("555 555 5555", true, '美国电话号码');
    t.equal("5555555555", true, '美国电话号码');
    t.equal("1 555 555 5555", true, '美国电话号码');
    t.equal("555-555-555asdf", false, '不是美国电话号码');
    t.equal("555)-555-5555", false, '不是美国电话号码');//这里容易错
    t.equal("(555-555-5555", false, '不是美国电话号码');//这里容易错
    t.end();
});
```

示例中有分隔为3+3+4形式的号码，因而改写正则，这里暂且假定分隔符为1个空格：`/\d{3} ?\d{3} ?\d{4}/`（注意中间有空格，问号?代表匹配0次或1次）

区号有且只有3位数，但可能被()包裹着，这里先处理括号。注意正则表达式中，括号尧转义（PS：顺带把空格改成\s）`/\(?\d{3}\)?\s?\d{3}\s?\d{4}/`，但是这个正则表达式有问题，只有半个括号的情况下，会return True，在这里加上情况`/(\(\d{3}\)|\d{3})\s?\d{3}\s?\d{4}/`

美国的国家代码为1，先考虑是否以1开头，并且考虑1后面可能有空格。`/^1?\s?(\(\d{3}\)|\d{3})\s?\d{3}\s?\d{4}/`

排除末尾加了奇奇怪怪字符的情况：`/^1?\s?(\(\d{3}\)|\d{3})\s?\d{3}\s?\d{4}$/`

有的地发空格可能是短横线：`/^1?\s?(\d{3}|\(\d{3}\))[ -]?\d{3}[ -]?\d{4}$/`

验证一下：

```js
function telephoneCheck(str) {return /^1?\s?(\d{3}|\(\d{3}\))[ -]?\d{3}[ -]?\d{4}$/.test(str);}
```

测试结果显示编写的函数如期运行，这样freecodecamp的高级算法第一题就完成了。

