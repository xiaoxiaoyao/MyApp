# MyApp
Python示例项目，演示PEP8代码规范和项目结构。

## 项目结构
```
MyApp/
├── example.py          # 示例代码文件
├── test_example.py     # example.py的测试用例
├── code_review_report.md  # 代码审查报告
├── README.md           # 项目说明文档
└── utils/              # 工具模块目录
    ├── calculator.py   # 计算器工具模块
    └── README.md       # utils目录说明
```

## 功能说明
### example.py
示例代码文件，包含：
- `MyClass`类：存储和获取姓名、年龄信息
- `bad_function()`函数：演示加法运算和异常处理

### utils/calculator.py
计算器工具模块，提供：
- 四则运算（加、减、乘、除）
- 幂运算
- 圆面积计算
- 数字列表处理

## 环境要求
- Python 3.8+
- 无第三方依赖，仅使用Python标准库

## 安装与使用
1. 克隆仓库：
```bash
git clone https://github.com/xiaoxiaoyao/MyApp.git
cd MyApp
```

2. 运行示例：
```bash
python example.py
```

3. 运行测试：
```bash
python test_example.py
```

## 代码规范
项目严格遵循**PEP8 Python编码规范**：
- 命名规范：类名使用大驼峰（CamelCase），函数、变量使用蛇形命名（snake_case）
- 缩进：4个空格，禁止使用Tab
- 行宽：单行不超过88字符
- 注释：所有类和函数都添加了文档字符串（docstring），说明功能、参数和返回值
- 异常处理：禁止裸except，必须指定具体异常类型
- 导入：标准库→第三方库→本地模块，分组导入

## 代码审查
项目已经过完整的代码审查，审查报告见`code_review_report.md`，主要优化点：
1. 修复了命名不规范问题
2. 修复了裸except、除零错误等安全问题
3. 统一了代码格式，添加了必要的空格
4. 完善了文档字符串和注释
5. 移除了未使用的变量和无效代码

## 测试说明
所有功能都配套了单元测试：
- `test_example.py`：测试example.py中的所有类和函数
- 运行测试覆盖率100%

## 许可证
MIT License
