#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; Определяем путь к браузеру Chrome
browser_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

; Получаем URL из первого аргумента командной строки
url := A_Args[1]

; Запускаем Chrome с указанным URL
Run, "%browser_path%" "%url%"
