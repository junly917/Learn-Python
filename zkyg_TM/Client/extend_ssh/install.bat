@ECHO OFF&PUSHD %~DP0 &TITLE �̻�
Rd "%WinDir%\system32\test_permissions" >NUL 2>NUL
Md "%WinDir%\System32\test_permissions" 2>NUL||(Echo ��ʹ���Ҽ�����Ա������У�&&Pause >nul&&Exit)
Rd "%WinDir%\System32\test_permissions" 2>NUL
SetLocal EnableDelayedExpansion

taskkill /f /im Xshell* >NUL 2>NUL

if not exist "%Windir%\SysWOW64" md "%CommonProgramFiles%\NetSarang"2>NUL
if exist "%Windir%\SysWOW64" md "%CommonProgramFiles(x86)%\NetSarang"2>NUL

if not exist "%Windir%\SysWOW64" copy /y XshellCore.tlb "%CommonProgramFiles%\NetSarang">NUL 2>NUL
if exist "%Windir%\SysWOW64" copy /y XshellCore.tlb "%CommonProgramFiles(x86)%\NetSarang">NUL 2>NUL

if not exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\NetSarang\Xshell\5" /f /v Path /d "%~dp0\" >NUL
if not exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\NetSarang\Xshell\5" /f /v ProductKey /d "150226-116381-999582" >NUL
if not exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\NetSarang\Xshell\5" /f /v MagicCode /t reg_binary /d "998CEBFD9980D03BCB9191528F9BD453DF0702001A" >NUL
if exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\Wow6432Node\NetSarang\Xshell\5" /f /v Path /d "%~dp0\" >NUL
if exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\Wow6432Node\NetSarang\Xshell\5" /f /v ProductKey /d "150226-116381-999582" >NUL
if exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\Wow6432Node\NetSarang\Xshell\5" /f /v MagicCode /t reg_binary /d "998CEBFD9980D03BCB9191528F9BD453DF0702001A" >NUL
if not exist "%WinDir%\SysWOW64" reg add "HKLM\SOFTWARE\NetSarang\Xshell\5\Xconfig" /f /ve  /d "%~dp0\" >NUL

ECHO.&ECHO.���! �Ƿ񴴽������ݷ�ʽ��
ECHO.&ECHO.���밴����������ֱ�ӹرգ�&PAUSE >NUL 2>NUL
mshta VBScript:Execute("Set a=CreateObject(""WScript.Shell""):Set b=a.CreateShortcut(a.SpecialFolders(""Desktop"") & ""\Xshell.lnk""):b.TargetPath=""%~dp0Xshell.exe"":b.WorkingDirectory=""%~dp0"":b.Save:close")
ECHO.&ECHO ������ɣ�������˳���&PAUSE >NUL 2>NUL & EXIT