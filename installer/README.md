# Banana Language 安装说明

## 安装方式

Banana语言提供三种安装方式，您可以根据需求选择：

### 1. 标准安装（推荐）

**文件：** `installer/install.bat`

**特点：**
- 需要管理员权限
- 安装到 `C:\Program Files\Banana`
- 可选择是否添加到系统PATH环境变量
- 创建桌面快捷方式和开始菜单快捷方式
- 适合长期使用和开发

**安装步骤：**
1. 右键点击 `install.bat`，选择"以管理员身份运行"
2. 按照提示完成安装
3. 选择是否添加到系统PATH（建议选择Y）
4. 安装完成后重启计算机或注销重新登录

**使用方法：**
- 如果添加了PATH：在任意位置运行 `banana <文件名.baNa>`
- 如果未添加PATH：使用完整路径 `C:\Program Files\Banana\banana.exe <文件名.baNa>`

### 2. 便携版安装

**文件：** `installer/install_portable.bat`

**特点：**
- 不需要管理员权限
- 安装到当前目录的 `Banana` 文件夹
- 不修改系统PATH
- 创建桌面快捷方式
- 适合临时使用或U盘携带

**安装步骤：**
1. 双击运行 `install_portable.bat`
2. 按照提示完成安装

**使用方法：**
- 双击桌面快捷方式
- 或运行 `Banana/banana.bat <文件名.baNa>`
- 或直接运行 `Banana/banana.exe <文件名.baNa>`

### 3. Inno Setup 安装程序

**文件：** `installer/banana_setup.iss`

**特点：**
- 专业的Windows安装程序
- 图形化安装界面
- 自动处理PATH环境变量
- 支持卸载程序
- 适合发布和分发

**使用方法：**
1. 需要先安装 [Inno Setup](https://jrsoftware.org/isdl.php)
2. 使用Inno Setup编译 `banana_setup.iss`
3. 运行生成的 `Banana-Setup-1.0.0.exe`

## 卸载

### 标准安装卸载

**文件：** `installer/uninstall.bat`

**卸载步骤：**
1. 右键点击 `uninstall.bat`，选择"以管理员身份运行"
2. 选择是否从系统PATH中移除（建议选择Y）
3. 确认卸载操作

### 便携版卸载

直接删除 `Banana` 文件夹即可。

### Inno Setup 安装程序卸载

使用Windows控制面板中的"程序和功能"卸载。

## 系统PATH说明

### 添加到PATH的好处
- 可以在任意位置运行 `banana` 命令
- 方便在命令行中使用
- 适合开发者和高级用户

### 不添加到PATH的情况
- 只在特定位置使用Banana语言
- 不想修改系统环境变量
- 使用便携版安装

### 手动添加到PATH
如果安装时未添加到PATH，可以手动添加：

1. 右键点击"此电脑"，选择"属性"
2. 点击"高级系统设置"
3. 点击"环境变量"
4. 在"系统变量"中找到"Path"，点击"编辑"
5. 点击"新建"，添加 `C:\Program Files\Banana`
6. 点击"确定"保存

## 验证安装

安装完成后，可以通过以下方式验证：

### 命令行验证
```bash
banana --version
```

### 运行示例程序
```bash
banana examples/hello.baNa
```

### 测试图形化功能
```bash
banana tests/simple_graphics_test.baNa
```

## 文件结构

安装后的文件结构：

```
C:\Program Files\Banana\
├── banana.exe              # 主程序
├── src\                    # 源代码
│   └── banana_interpreter_simple.py
├── mode\                   # 模块
│   └── graphics.BMDe
├── tests\                  # 测试文件
│   ├── test_graphics.baNa
│   └── simple_graphics_test.baNa
├── examples\               # 示例程序
│   └── hello.baNa
├── docs\                   # 文档
│   └── README.md
├── resources\              # 资源文件
│   └── logo.ico
├── README.md               # 说明文档
└── LICENSE                 # 许可证
```

## 常见问题

### Q: 安装后无法运行banana命令？
A: 请确保：
1. 已重启计算机或注销重新登录
2. 已添加到系统PATH环境变量
3. 使用完整路径测试：`C:\Program Files\Banana\banana.exe`

### Q: 图形化功能无法使用？
A: 请确保：
1. 已安装Python的turtle模块
2. 运行测试程序：`banana tests/simple_graphics_test.baNa`
3. 检查是否有防火墙阻止

### Q: 如何更新Banana语言？
A: 下载新版本后，运行卸载程序，然后重新安装即可。

### Q: 便携版和标准版有什么区别？
A: 主要区别：
- 便携版不需要管理员权限
- 便携版不修改系统PATH
- 便携版可以放在U盘上使用
- 标准版更适合长期使用

## 技术支持

如有问题，请访问：
- GitHub: https://github.com/banana-language
- Issues: https://github.com/banana-language/issues
- 文档: `docs/README.md`

## 许可证

Banana Language 遵循 MIT 许可证。详见 LICENSE 文件。
