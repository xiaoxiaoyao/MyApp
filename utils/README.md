# utils 工具目录
## 功能说明
存放项目的通用工具模块，提供可复用的功能函数和类。

## 模块列表
### calculator.py
**功能**：计算器工具模块
- 提供`Calculator`类，封装了加法、减法、乘法、除法、幂运算
- 提供`calculate_area()`函数：计算圆的面积
- 提供`process_data()`函数：处理数字列表，正数乘2，非正数置0

## 依赖
- Python 标准库 `math`

## 使用示例
```python
from utils.calculator import Calculator, calculate_area, process_data

# 使用计算器类
calc = Calculator()
print(calc.add(1, 2))  # 输出：3
print(calc.divide(10, 2))  # 输出：5.0

# 计算圆面积
print(calculate_area(5))  # 输出：78.53981633974483

# 处理数据列表
print(process_data([-1, 2, 3, -4, 5]))  # 输出：[0, 4, 6, 0, 10]
```

## 注意事项
- 所有方法和函数都添加了类型提示，便于IDE自动补全和静态检查
- 除法运算会抛出`ValueError`异常当除数为0
