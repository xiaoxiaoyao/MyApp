# python_unittest 目录

本目录包含 Python 单元测试的学习和实践代码，主要演示如何使用 Python 标准库中的 unittest 模块进行单元测试。

## 主要文件

### mathfunc.py
- **用途**：数学运算函数实现
- **内容**：
  - 加法函数：`add(a, b)`
  - 减法函数：`minus(a, b)`
  - 乘法函数：`multi(a, b)`
  - 特殊乘法函数：`multi_not_zero(a, b)`（禁止乘数为0）
  - 除法函数：`divide(a, b)`
  - 自定义异常类：`ZeroMultiError`

### mathfunc 相关说明
- 所有函数都严格遵循 PEP 8 规范
- 每个函数都有完整的中文文档字符串（docstring）
- 使用类型注解提高代码可读性
- 包含详细的异常处理

## 测试方法

```bash
# 运行所有测试
python -m unittest mathfunc
```

## 学习资源
- Python 单元测试官方文档：https://docs.python.org/3/library/unittest.html