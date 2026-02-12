@echo off
chcp 65001 >nul
echo ========================================
echo   Banana Language 便携版安装程序 v1.0.0
echo ========================================
echo.

REM 设置安装路径
set "INSTALL_DIR=%~dp0Banana"
set "SCRIPT_DIR=%~dp0"

echo [1/4] 创建安装目录...
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
    echo   ✓ 创建目录: %INSTALL_DIR%
) else (
    echo   ✓ 目录已存在: %INSTALL_DIR%
)

echo.
echo [2/4] 复制文件到安装目录...

REM 复制主程序
copy "%SCRIPT_DIR%bin\banana.exe" "%INSTALL_DIR%\" >nul
echo   ✓ 复制 banana.exe

REM 创建源代码目录
if not exist "%INSTALL_DIR%\src" mkdir "%INSTALL_DIR%\src"
xcopy "%SCRIPT_DIR%src\*.py" "%INSTALL_DIR%\src\" /Y /Q >nul 2>&1
echo   ✓ 复制源代码文件

REM 创建模块目录
if not exist "%INSTALL_DIR%\mode" mkdir "%INSTALL_DIR%\mode"
xcopy "%SCRIPT_DIR%mode\*.BMDe" "%INSTALL_DIR%\mode\" /Y /Q >nul 2>&1
echo   ✓ 复制模块文件

REM 创建测试目录
if not exist "%INSTALL_DIR%\tests" mkdir "%INSTALL_DIR%\tests"
xcopy "%SCRIPT_DIR%tests\*.baNa" "%INSTALL_DIR%\tests\" /Y /Q >nul 2>&1
echo   ✓ 复制测试文件

REM 创建示例目录
if not exist "%INSTALL_DIR%\examples" mkdir "%INSTALL_DIR%\examples"
xcopy "%SCRIPT_DIR%examples\*.baNa" "%INSTALL_DIR%\examples\" /Y /Q >nul 2>&1
echo   ✓ 复制示例文件

REM 创建文档目录
if not exist "%INSTALL_DIR%\docs" mkdir "%INSTALL_DIR%\docs"
xcopy "%SCRIPT_DIR%docs\*" "%INSTALL_DIR%\docs\" /Y /E /I /Q >nul 2>&1
echo   ✓ 复制文档文件

REM 创建资源目录
if not exist "%INSTALL_DIR%\resources" mkdir "%INSTALL_DIR%\resources"
xcopy "%SCRIPT_DIR%resources\*" "%INSTALL_DIR%\resources\" /Y /E /I /Q >nul 2>&1
echo   ✓ 复制资源文件

REM 复制README和LICENSE
if exist "%SCRIPT_DIR%README.md" copy "%SCRIPT_DIR%README.md" "%INSTALL_DIR%\" >nul
if exist "%SCRIPT_DIR%LICENSE" copy "%SCRIPT_DIR%LICENSE" "%INSTALL_DIR%\" >nul

echo.
echo [3/4] 创建启动脚本...

REM 创建启动脚本
(
echo @echo off
echo chcp 65001 ^>nul
echo set "BANANA_HOME=%INSTALL_DIR:\=/%"
echo set "PATH=%%PATH%%;%%BANANA_HOME%%"
echo "%%BANANA_HOME%%\banana.exe" %%*
) > "%INSTALL_DIR%\banana.bat"
echo   ✓ 已创建 banana.bat

echo.
echo [4/4] 创建桌面快捷方式...

set "DESKTOP=%USERPROFILE%\Desktop"
set "SHORTCUT=%DESKTOP%\Banana Language (Portable).lnk"

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT%'); $s.TargetPath = '%INSTALL_DIR%\banana.bat'; $s.WorkingDirectory = '%INSTALL_DIR%'; $s.Description = 'Banana Programming Language (Portable)'; $s.Save()"
echo   ✓ 已创建桌面快捷方式

echo.
echo ========================================
echo   便携版安装完成！
echo ========================================
echo.
echo 安装位置: %INSTALL_DIR%
echo.
echo 使用说明：
echo 1. 便携版不需要管理员权限
echo 2. 直接运行桌面快捷方式或 %INSTALL_DIR%\banana.bat
echo 3. 示例文件位于: %INSTALL_DIR%\examples
echo 4. 文档位于: %INSTALL_DIR%\docs
echo 5. 如需卸载，直接删除 %INSTALL_DIR% 文件夹即可
echo.
echo 按任意键退出...
pause >nul
