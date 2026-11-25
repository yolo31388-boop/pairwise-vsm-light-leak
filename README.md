# pairwise-vsm-light-leak

## 领域

游戏、图形与多媒体

## 主题

方差阴影图漏光抑制

## 说明

矩精度补偿、mip 半影核、双缓冲代际。

初始状态下 `graphics/variance_shadow.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
