# 分支管理规范与变更历史

## 分支命名规范

### 基本格式
```
<分支类型前缀>/<描述性名称>#<可选任务ID>
```

### 分支类型前缀
- `feature/`：新功能开发
- `bugfix/`：缺陷修复
- `hotfix/`：紧急修复
- `refactor/`：代码重构
- `docs/`：文档更新
- `test/`：测试相关

### 命名要求
- 使用小写字母
- 多个单词用连字符(-)连接
- 分支名称长度控制在50字符以内
- 名称应准确反映开发目的或修改内容

### 示例
- `feature/user-authentication`
- `bugfix/login-validation`
- `hotfix/security-patch#123`

## 分支变更历史

| 变更前分支名称 | 变更后分支名称 | 变更时间 | 变更原因 | 操作人 |
|----------------|----------------|----------|----------|--------|
| `optimize/code-quality-20260323` | `refactor/code-quality-20260323` | 2026-04-08 14:30 | 符合分支命名规范，将optimize前缀改为refactor | CodeReview Bot |
| `optimize/code-quality-20260326` | `refactor/code-quality-20260326` | 2026-04-08 14:31 | 符合分支命名规范，将optimize前缀改为refactor | CodeReview Bot |
| `feature/code-optimization` | `refactor/code-optimization` | 2026-04-08 14:32 | 符合分支命名规范，将feature前缀改为refactor | CodeReview Bot |
