; Проверка административных прав
If not A_IsAdmin
{
    ; Повторный запуск с правами администратора
    Run *RunAs "%A_ScriptFullPath%"
    ; Выход из текущего экземпляра скрипта
    ExitApp
}


; Set partial title matching mode
SetTitleMatchMode, 2

; List of all browsers to close
GroupAdd, browsers, ahk_class MozillaWindowClass
GroupAdd, browsers, ahk_class IEFrame
GroupAdd, browsers, ahk_exe msedge.exe
GroupAdd, browsers, ahk_exe chrome.exe
GroupAdd, browsers, ahk_exe firefox.exe

; Loop through each browser window and close it
GroupClose, browsers
