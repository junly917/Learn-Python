@ECHO OFF& TITLE ж��
taskkill /f /im Xshell* >NUL 2>NUL
rd/s/q "%ProgramData%\NetSarang" 2>NUL
rd/s/q "%AllUsersProfile%\NetSarang"2>NUL
reg delete HKLM\SOFTWARE\NetSarang /F>NUL 2>NUL
reg delete HKLM\SOFTWARE\Wow6432Node\NetSarang /F>NUL 2>NUL
ECHO.&ECHO.���, �Ƿ���Ҫ�����������ݣ�
ECHO.&ECHO.��ֱ�ӹرգ��������������&PAUSE >NUL 2>NUL
for /f "skip=2 tokens=3 delims= " %%i in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v personal') do (
       for /f "delims=*" %%j in ('echo %%i') do rd/s/q "%%j\NetSarang" 2>NUL)
reg delete HKCU\Software\NetSarang /F>NUL 2>NUL
ECHO.&ECHO ж����ɣ�������˳���&PAUSE >NUL 2>NUL & EXIT