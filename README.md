# Banana Language v1.0.0

## 简介

Banana（香蕉语言）是一个简单易学的编程语言，支持基本的编程功能，包括变量、函数、控制流等。特别之处在于它内置了图形化库，可以轻松创建图形和动画效果。

## 特性

- **简单易学**：语法简洁，适合初学者
- **图形化支持**：内置图形库，支持绘制各种图形
- **模块化**：支持自定义模块和Python模块导入
- **跨平台**：基于Python开发，可在Windows、Linux、Mac上运行
- **中文友好**：支持中文注释和输出

## 安装

### 快速安装

1. **标准安装**（推荐）
   - 右键点击 `installer/install.bat`，选择"以管理员身份运行"
   - 按照提示完成安装
   - 选择是否添加到系统PATH（建议选择Y）
   - 重启计算机使PATH生效

2. **便携版安装**
   - 双击运行 `installer/install_portable.bat`
   - 按照提示完成安装
   - 无需管理员权限

详细安装说明请参考 [installer/README.md](installer/README.md)

## 快速开始

### Hello World

创建文件 `hello.baNa`：

```banana
banana

println("Hello, World!")

end
```

运行：
```bash
banana hello.baNa
```

### 图形化示例

```banana
banana

import graphics

init_graphics()
draw_rectangle(-100, 100, 200, 200)
draw_circle(0, 0, 50)

input("按Enter退出...")
close_graphics()

end
```

## 语法参考

### 基本结构

```banana
banana

# 你的代码

end
```

### 变量

```banana
let name = "Banana"
let age = 18
let pi = 3.14159
```

### 输入输出

```banana
println("Hello, World!")
print("输入你的名字: ")
let name = input()
let num = input_num("输入一个数字: ")
```

### 条件语句

```banana
if age >= 18:
    println("成年人")
else:
    println("未成年人")
endif
```

### 循环

```banana
# for循环
for i in 1 to 10:
    println(i)
endfor

# while循环
let i = 0
while i < 10:
    println(i)
    i = i + 1
endwhile
```

### 函数

```banana
func add(a, b)
    return a + b
endfunc

let result = add(3, 5)
println(result)
```

### 列表

```banana
let numbers = [1, 2, 3, 4, 5]
let fruits = ["apple", "banana", "orange"]

println(len(numbers))
println(sum(numbers))
```

### 导入模块

```banana
# 导入自定义模块
import graphics

# 导入Python模块
import turtle
import random
```

## 图形化库

### 基本函数

```banana
# 初始化图形系统
init_graphics()

# 关闭图形系统
close_graphics()

# 清屏
clear_screen()
```

### 绘制图形

```banana
# 绘制矩形
draw_rectangle(x, y, width, height)
fill_rectangle(x, y, width, height, color)

# 绘制圆形
draw_circle(x, y, radius)
fill_circle(x, y, radius, color)

# 绘制三角形
draw_triangle(x1, y1, x2, y2, x3, y3)
fill_triangle(x1, y1, x2, y2, x3, y3, color)

# 绘制线
draw_line(x1, y1, x2, y2, color, size)

# 绘制点
draw_point(x, y, size, color)

# 绘制文本
draw_text(x, y, text, size, color)
```

### 辅助函数

```banana
# 绘制网格
draw_grid(size, color)

# 绘制坐标轴
draw_coordinates()

# 随机颜色
let color = random_color()

# 延迟
delay(seconds)
```

### 完整示例

```banana
banana

import graphics

init_graphics()

# 绘制彩色圆形
for i in 1 to 10:
    let x = random.randint(-300, 300)
    let y = random.randint(-200, 200)
    let r = random.randint(20, 50)
    let color = random_color()
    fill_circle(x, y, r, color)
endfor

draw_text(0, 0, "Banana Graphics!", 24, "black")

input("按Enter退出...")
close_graphics()

end
```

## 内置函数

### 数学函数

- `abs(x)` - 绝对值
- `sqrt(x)` - 平方根
- `sin(x)` - 正弦
- `cos(x)` - 余弦
- `tan(x)` - 正切
- `log(x)` - 自然对数
- `exp(x)` - 指数
- `pow(x, y)` - 幂运算
- `rand()` - 随机数

### 字符串函数

- `len(s)` - 字符串长度
- `str(x)` - 转换为字符串
- `int(s)` - 转换为整数
- `float(s)` - 转换为浮点数

### 列表函数

- `len(list)` - 列表长度
- `max(list)` - 最大值
- `min(list)` - 最小值
- `sum(list)` - 求和

## 示例程序

项目包含多个示例程序，位于 `examples/` 目录：

- `hello.baNa` - Hello World 示例
- `calculator.baNa` - 简单计算器
- 更多示例...

运行示例：
```bash
banana examples/hello.baNa
```

## 测试

项目包含测试程序，位于 `tests/` 目录：

- `test_graphics.baNa` - 图形化测试
- `simple_graphics_test.baNa` - 简单图形测试

运行测试：
```bash
banana tests/simple_graphics_test.baNa
```

## 项目结构

```
Banana-1.0.0/
├── bin/                    # 可执行文件
│   ├── banana.exe         # 主程序
│   └── banana.bat         # 启动脚本
├── src/                    # 源代码
│   └── banana_interpreter_simple.py
├── mode/                   # 模块
│   └── graphics.BMDe      # 图形化模块
├── tests/                  # 测试文件
│   ├── test_graphics.baNa
│   └── simple_graphics_test.baNa
├── examples/               # 示例程序
│   ├── hello.baNa
│   └── calculator.baNa
├── docs/                   # 文档
│   └── README.md
├── resources/              # 资源文件
│   └── logo.ico
├── installer/              # 安装程序
│   ├── install.bat        # 标准安装
│   ├── install_portable.bat # 便携版安装
│   ├── uninstall.bat      # 卸载程序
│   ├── banana_setup.iss   # Inno Setup配置
│   └── README.md         # 安装说明
├── README.md              # 本文件
└── LICENSE               # 许可证
```

## 卸载

### 标准安装卸载

右键点击 `installer/uninstall.bat`，选择"以管理员身份运行"

### 便携版卸载

直接删除安装目录即可

## 常见问题

### Q: 如何运行.baNa文件？
A: 安装后，在命令行中运行 `banana <文件名.baNa>`

### Q: 图形化功能无法使用？
A: 确保已安装Python的turtle模块，运行测试程序验证

### Q: 如何添加到PATH？
A: 安装时选择添加到PATH，或手动添加 `C:\Program Files\Banana` 到系统PATH

### Q: 支持哪些操作系统？
A: 支持Windows、Linux、Mac（需要Python环境）

## 技术支持

- GitHub: https://github.com/banana-language
- Issues: https://github.com/banana-language/issues
- 文档: docs/README.md

## 许可证

Banana Language 遵循 MIT 许可证。详见 LICENSE 文件。

## 贡献

欢迎贡献代码、报告问题或提出建议！

## 更新日志

### v1.0.0 (2024-02-11)
- 初始版本发布
- 支持基本语法
- 内置图形化库
- 支持模块导入
- 提供安装程序

---

**Banana Language** - 让编程变得简单有趣！
