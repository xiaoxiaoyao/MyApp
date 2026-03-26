# TDD - 测试驱动开发目录

本目录包含项目的所有测试用例，使用 Python 的 unittest 框架编写。

## 目录结构

```
TDD/
├── README.md                 # 本文件
├── run_all_tests.py         # 测试运行脚本
├── test_calculator.py       # calculator.py 的测试用例
├── test_example.py          # example.py 的测试用例
├── python_unittest/         # Python unittest 示例
└── UnitTestDrivenDevelopment/  # 单元测试驱动开发示例
```

## 测试文件说明

### test_calculator.py
测试 `utils/calculator.py` 模块，包含以下测试类：
- **TestCalculatorBasic**: 基础功能测试（加减乘除、幂运算）
- **TestCalculatorEdgeCases**: 边界条件测试（大数、小数、精度）
- **TestCalculateArea**: 圆面积计算函数测试
- **TestProcessData**: 数据处理函数测试
- **TestCalculatorIntegration**: 集成测试（链式运算）

### test_example.py
测试 `example.py` 模块，包含以下测试类：
- **TestMyClass**: MyClass 类的单元测试
- **TestBadFunction**: bad_function 函数的测试
- **TestMyClassIntegration**: MyClass 集成测试
- **TestEdgeCases**: 边界条件测试

## 运行测试

### 运行所有测试
```bash
cd /root/.openclaw/workspace/MyApp/TDD
python run_all_tests.py
```

### 运行单个测试文件
```bash
cd /root/.openclaw/workspace/MyApp/TDD
python test_calculator.py
python test_example.py
```

### 使用 unittest 模块运行
```bash
cd /root/.openclaw/workspace/MyApp
python -m unittest TDD.test_calculator
python -m unittest TDD.test_example
```

## 测试覆盖率

### calculator.py 测试覆盖
- ✅ 加法运算（正数、负数、零、浮点数）
- ✅ 减法运算（正数、负数、零）
- ✅ 乘法运算（正数、负数、零）
- ✅ 除法运算（正数、负数、除零异常）
- ✅ 幂运算（正指数、零指数、负指数）
- ✅ 圆面积计算（正半径、零半径、大半径）
- ✅ 数据处理（正数、负数、零、混合、空列表）

### example.py 测试覆盖
- ✅ MyClass 初始化
- ✅ set_name 方法（正常值、空值、中文、特殊字符）
- ✅ get_info 方法（默认值、设置后）
- ✅ age 属性修改
- ✅ bad_function 函数
- ✅ 边界条件（超长字符串、大数）

## 测试规范

### 命名规范
- 测试文件：`test_<模块名>.py`
- 测试类：`Test<被测类名>` 或 `Test<功能描述>`
- 测试方法：`test_<被测方法>_<场景描述>`

### 测试结构
```python
class TestExample(unittest.TestCase):
    def setUp(self):
        """测试前初始化"""
        pass
    
    def tearDown(self):
        """测试后清理"""
        pass
    
    def test_feature_normal(self):
        """测试正常场景"""
        pass
    
    def test_feature_edge_case(self):
        """测试边界条件"""
        pass
```

### 断言方法
- `assertEqual(a, b)` - 相等
- `assertNotEqual(a, b)` - 不相等
- `assertTrue(x)` - 为真
- `assertFalse(x)` - 为假
- `assertIsNone(x)` - 为 None
- `assertIsNotNone(x)` - 不为 None
- `assertIn(a, b)` - 包含
- `assertNotIn(a, b)` - 不包含
- `assertIsInstance(a, b)` - 类型检查
- `assertRaises(Exception)` - 异常检查

## 添加新测试

1. 创建测试文件 `test_<模块名>.py`
2. 导入被测模块：`from <模块路径> import <类/函数>`
3. 创建测试类继承 `unittest.TestCase`
4. 编写测试方法
5. 运行测试验证

## 目标

- 测试覆盖率：100%
- 测试通过率：100%
- 所有边界条件覆盖
- 所有异常场景覆盖
