@echo off
chcp 65001 >nul
echo ========================================
echo   Banana Language 卸载程序 v1.0.0
echo ========================================
echo.

REM 检查管理员权限
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [错误] 需要管理员权限运行此卸载程序
    echo 请右键点击此文件，选择"以管理员身份运行"
    pause
    exit /b 1
)

set "INSTALL_DIR=C:\Program Files\Banana"

REM 确认卸载
echo 警告：此操作将从系统中完全移除 Banana Language
echo 安装位置: %INSTALL_DIR%
echo.
set /p CONFIRM="确认卸载？(Y/N): "
if /i not "%CONFIRM%"=="Y" (
    echo 卸载已取消
    pause
    exit /b 0
)

echo.
echo [1/4] 从系统PATH中移除...

REM 询问用户是否从PATH中移除
set /p REMOVE_PATH="是否从系统PATH环境变量中移除？(Y/N): "
if /i "%REMOVE_PATH%"=="Y" (
    REM 获取当前PATH
    for /f "tokens=2*" %%A in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "CURRENT_PATH=%%B"
    
    REM 移除安装目录
    set "NEW_PATH=%CURRENT_PATH%"
    set "NEW_PATH=%NEW_PATH:;%INSTALL_DIR%=%"
    set "NEW_PATH=%NEW_PATH:%INSTALL_DIR%;=%"
    set "NEW_PATH=%NEW_PATH:%INSTALL_DIR%=%"
    
    setx PATH "%NEW_PATH%" /M >nul
    echo   ✓ 已从系统PATH中移除
) else (
    echo   ✓ 跳过从系统PATH中移除
)

echo.
echo [2/4] 删除桌面快捷方式...

set "DESKTOP=%USERPROFILE%\Desktop"
if exist "%DESKTOP%\Banana Language.lnk" (
    del "%DESKTOP%\Banana Language.lnk"
    echo   ✓ 已删除桌面快捷方式
) else (
    echo   ✓ 桌面快捷方式不存在
)

echo.
echo [3/4] 删除开始菜单快捷方式...

set "STARTMENU=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Banana Language"
if exist "%STARTMENU%" (
    rmdir /s /q "%STARTMENU%"
    echo   ✓ 已删除开始菜单快捷方式
) else (
    echo   ✓ 开始菜单快捷方式不存在
)

echo.
echo [4/4] 删除安装目录...

if exist "%INSTALL_DIR%" (
    rmdir /s /q "%INSTALL_DIR%"
    echo   ✓ 已删除安装目录
) else (
    echo   ✓ 安装目录不存在
)

echo.
echo ========================================
echo   卸载完成！
echo ========================================
echo.
echo 重要提示：
echo 请重启计算机或注销并重新登录以使PATH环境变量生效
echo.
echo 按任意键退出...
pause >nul
