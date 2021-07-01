@echo off
set path=c:\programs\mingw\bin;C:\Users\u1273400\AppData\Local\Programs\Microsoft VS Code\bin;C:\Users\u1273400\AppData\Local\Programs\git\bin
rem if x%Path:g++=%==x%Path% set PATH=%PATH%;%str1%
mingw32-make %1
