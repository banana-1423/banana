@echo off
chcp 65001 >nul
echo ========================================
echo   Banana Language 安装程序 v1.0.0
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [错误] 需要管理员权限运行此安装程序
    echo 请右键点击此文件，选择"以管理员身份运行"
    pause
    exit /b 1
)

REM 设置安装路径
set "INSTALL_DIR=C:\Program Files\Banana"
set "SCRIPT_DIR=%~dp0"

echo [1/5] 创建安装目录...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo   ✓ 创建目录: %INSTALL_DIR%
) else (
    echo   ✓ 目录已存在: %INSTALL_DIR%
)

echo.
echo [2/5] 复制文件到安装目录...

REM 复制主程序
copy "%SCRIPT_DIR%..\bin\banana.exe" "%INSTALL_DIR%\" >nul
echo   ✓ 复制 banana.exe

REM 创建源代码目录
if not exist "%INSTALL_DIR%\src" mkdir "%INSTALL_DIR%\src"
xcopy "%SCRIPT_DIR%..\src\*.py" "%INSTALL_DIR%\src\" /Y /Q >nul 2>&1
echo   ✓ 复制源代码文件

REM 创建模块目录
if not exist "%INSTALL_DIR%\mode" mkdir "%INSTALL_DIR%\mode"
xcopy "%SCRIPT_DIR%..\mode\*.BMDe" "%INSTALL_DIR%\mode\" /Y /Q >nul 2>&1
echo   ✓ 复制模块文件

REM 创建测试目录
if not exist "%INSTALL_DIR%\tests" mkdir "%INSTALL_DIR%\tests"
xcopy "%SCRIPT_DIR%..\tests\*.baNa" "%INSTALL_DIR%\tests\" /Y /Q >nul 2>&1
echo   ✓ 复制测试文件

REM 创建示例目录
if not exist "%INSTALL_DIR%\examples" mkdir "%INSTALL_DIR%\examples"
xcopy "%SCRIPT_DIR%..\examples\*.baNa" "%INSTALL_DIR%\examples\" /Y /Q >nul 2>&1
echo   ✓ 复制示例文件

REM 创建文档目录
if not exist "%INSTALL_DIR%\docs" mkdir "%INSTALL_DIR%\docs"
xcopy "%SCRIPT_DIR%..\docs\*" "%INSTALL_DIR%\docs\" /Y /E /I /Q >nul 2>&1
echo   ✓ 复制文档文件

REM 创建资源目录
if not exist "%INSTALL_DIR%\resources" mkdir "%INSTALL_DIR%\resources"
xcopy "%SCRIPT_DIR%..\resources\*" "%INSTALL_DIR%\resources\" /Y /E /I /Q >nul 2>&1
echo   ✓ 复制资源文件

REM 复制README和LICENSE
if exist "%SCRIPT_DIR%..\README.md" copy "%SCRIPT_DIR%..\README.md" "%INSTALL_DIR%\" >nul
if exist "%SCRIPT_DIR%..\LICENSE" copy "%SCRIPT_DIR%..\LICENSE" "%INSTALL_DIR%\" >nul

echo.
echo [3/5] 添加到系统PATH环境变量...

REM 询问用户是否添加到PATH
set /p ADD_PATH="是否添加到系统PATH环境变量？(Y/N): "
if /i "%ADD_PATH%"=="Y" (
    REM 获取当前PATH
    for /f "tokens=2*" %%A in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "CURRENT_PATH=%%B"
    
    REM 检查是否已经添加
    echo %CURRENT_PATH% | find /i "%INSTALL_DIR%" >nul
    if %errorLevel% neq 0 (
        setx PATH "%CURRENT_PATH%;%INSTALL_DIR%" /M >nul
        echo   ✓ 已添加到系统PATH
    ) else (
        echo   ✓ 已在PATH中，跳过
    )
) else (
    echo   ✓ 跳过添加到系统PATH
    echo.
    echo   提示：您可以通过以下方式使用Banana语言：
    echo   1. 使用完整路径: %INSTALL_DIR%\banana.exe
    echo   2. 创建批处理文件调用banana.exe
    echo   3. 手动将 %INSTALL_DIR% 添加到PATH
)

echo.
echo [4/5] 创建桌面快捷方式...

set "DESKTOP=%USERPROFILE%\Desktop"
set "SHORTCUT=%DESKTOP%\Banana Language.lnk"

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT%'); $s.TargetPath = '%INSTALL_DIR%\banana.exe'; $s.WorkingDirectory = '%INSTALL_DIR%'; $s.Description = 'Banana Programming Language'; $s.Save()"
echo   ✓ 已创建桌面快捷方式

echo.
echo [5/5] 创建开始菜单快捷方式...

set "STARTMENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Banana Language"
if not exist "%STARTMENU%" mkdir "%STARTMENU%"

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTMENU%\Banana Language.lnk'); $s.TargetPath = '%INSTALL_DIR%\banana.exe'; $s.WorkingDirectory = '%INSTALL_DIR%'; $s.Description = 'Banana Programming Language'; $s.Save()"
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTMENU%\Banana Documentation.lnk'); $s.TargetPath = '%INSTALL_DIR%\docs\README.md'; $s.WorkingDirectory = '%INSTALL_DIR%\docs'; $s.Description = 'Banana Documentation'; $s.Save()"
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%STARTMENU%\Banana Examples.lnk'); $s.TargetPath = '%INSTALL_DIR%\examples'; $s.WorkingDirectory = '%INSTALL_DIR%\examples'; $s.Description = 'Banana Examples'; $s.Save()"
echo   ✓ 已创建开始菜单快捷方式

echo.
echo ========================================
echo   安装完成！
echo ========================================
echo.
echo 安装位置: %INSTALL_DIR%
echo.
echo 重要提示：
echo 1. 请重启计算机或注销并重新登录以使PATH环境变量生效
echo 2. 重启后，您可以在任何位置运行 "banana <文件名.baNa>" 来执行Banana程序
echo 3. 示例文件位于: %INSTALL_DIR%\examples
echo 4. 文档位于: %INSTALL_DIR%\docs
echo.
echo 按任意键退出...
pause >nul
