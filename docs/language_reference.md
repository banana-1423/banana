# Banana语言参考手册

## 1. 概述

Banana语言（香蕉语言）是一种简单的脚本编程语言，设计用于学习编程概念和解释器开发。

## 2. 基本语法

### 2.1 程序结构

Banana语言程序的基本结构如下：

```banana
banana
# 程序代码
end
```

- `banana` - 程序开始标记
- `end` - 程序结束标记

### 2.2 注释

使用 `#` 符号表示单行注释：

```banana
# 这是一条注释
let x = 10  # 这也是一条注释
```

## 3. 变量

### 3.1 变量定义

使用 `let` 关键字定义变量：

```banana
let name = "Banana"
let age = 10
let score = 95.5
```

### 3.2 变量修改

使用 `set` 关键字修改变量：

```banana
let x = 10
set x = 20
```

## 4. 数据类型

Banana语言支持以下基本数据类型：

- **字符串**：用双引号包围的文本，如 `"Hello"`
- **数字**：整数或浮点数，如 `10`、`3.14`
- **列表**：用 `list()` 函数创建的有序集合，如 `list(1, 2, 3)`

## 5. 运算符

### 5.1 算术运算符

- `+` - 加法
- `-` - 减法
- `*` - 乘法
- `/` - 除法
- `%` - 取模

### 5.2 比较运算符

- `>` - 大于
- `<` - 小于
- `==` - 等于

## 6. 控制流

### 6.1 条件语句

```banana
if 条件
    # 条件为真时执行的代码
else
    # 条件为假时执行的代码
endif
```

### 6.2 循环语句

```banana
for 变量 in 列表
    # 循环体代码
endfor
```

## 7. 函数

### 7.1 函数定义

```banana
func 函数名(参数1, 参数2, ...)
    # 函数体代码
    return 返回值
endfunc
```

### 7.2 函数调用

```banana
let 结果 = 函数名(参数1, 参数2, ...)
```

## 8. 内置函数

### 8.1 输出函数

- `print(表达式)` - 打印内容（不换行）
- `println(表达式)` - 打印内容（换行）

### 8.2 输入函数

- `input(提示)` - 输入字符串
- `input_num(提示)` - 输入数字

### 8.3 类型转换函数

- `str(表达式)` - 转换为字符串
- `int(表达式)` - 转换为整数
- `float(表达式)` - 转换为浮点数

### 8.4 列表函数

- `list(元素1, 元素2, ...)` - 创建列表
- `len(列表)` - 获取列表长度
- `max(列表)` - 获取列表最大值
- `min(列表)` - 获取列表最小值
- `sum(列表)` - 获取列表总和

### 8.5 其他函数

- `rand()` - 生成随机数（0-1）

## 9. 示例程序

### 9.1 简单的Hello World

```banana
banana
println("Hello, Banana World!")
end
```

### 9.2 计算平均数

```banana
banana
func calculate_average(numbers)
    let total = sum(numbers)
    let count = len(numbers)
    if count > 0
        return total / count
    else
        return 0
    endif
endfunc

let scores = list(85, 92, 78, 90, 88)
let avg = calculate_average(scores)
println("平均成绩: " + str(avg))
end
```

## 10. 运行Banana程序

### 10.1 使用命令行工具

```bash
# 使用bin目录中的脚本
bin/banana <file.banana>

# 直接运行解释器
python src/banana_interpreter_simple.py <file.banana>
```

### 10.2 示例

```bash
# 运行Hello World示例
bin/banana examples/hello_world.banana

# 运行斐波那契数列示例
bin/banana examples/fibonacci.banana
```
