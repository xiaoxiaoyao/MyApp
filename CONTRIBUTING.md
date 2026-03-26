# contributing.md：如何参与项目贡献代码？

WELCOME ！

## everything is ok

写啥都可以，大家开心我就开心啦~

点击[我的知乎](https://www.zhihu.com/question/59524525/answer/213532626)或者直接Github给我提交任何东西都没问题。直接发email也没问题。没啥要求，开心就好～

## 自动化测试流程

### 测试环境
- 使用 GitHub Actions 进行 CI 测试
- 测试在 Ubuntu 最新版本上运行
- 使用 Python 3.9

### 测试触发条件
- 代码推送到 `master` 分支
- 代码推送到 `optimize/code-quality-20260326` 分支
- 创建或更新针对 `master` 分支的 Pull Request

### 运行测试

#### 本地运行
```bash
# 运行所有测试
python run_all_tests.py

# 运行单个测试文件
python -m unittest TDD.test_calculator
python -m unittest TDD.test_example
```

#### 测试覆盖范围
- 核心工具模块（calculator, example）
- 算法和数据结构（汉诺塔, 杨辉三角）
- Web 应用功能
- 常用工具函数
- 文件操作和网络操作

### 测试文件位置
所有测试文件都放在 `TDD` 目录下：
- `TDD/test_all_modules.py` - 全面测试所有模块
- `TDD/test_calculator.py` - 计算器模块测试
- `TDD/test_example.py` - 示例模块测试
- `TDD/test_basic.py` - 基础功能测试
- `TDD/test_core_modules.py` - 核心模块测试

### 提交代码前的建议
1. 运行本地测试确保代码通过
2. 确保代码符合项目的代码规范
3. 为新功能添加相应的测试用例
