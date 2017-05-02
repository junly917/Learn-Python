@ECHO OFF& TITLE 卸载
taskkill /f /im Xshell* >NUL 2>NUL
rd/s/q "%ProgramData%\NetSarang" 2>NUL
rd/s/q "%AllUsersProfile%\NetSarang"2>NUL
reg delete HKLM\SOFTWARE\NetSarang /F>NUL 2>NUL
reg delete HKLM\SOFTWARE\Wow6432Node\NetSarang /F>NUL 2>NUL
ECHO.&ECHO.完成, 是否需要清理配置数据？
ECHO.&ECHO.是直接关闭，否按任意键继续！&PAUSE >NUL 2>NUL
for /f "skip=2 tokens=3 delims= " %%i in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v personal') do (
       for /f "delims=*" %%j in ('echo %%i') do rd/s/q "%%j\NetSarang" 2>NUL)
reg delete HKCU\Software\NetSarang /F>NUL 2>NUL
ECHO.&ECHO 卸载完成，任意键退出！&PAUSE >NUL 2>NUL & EXIT