@echo off

set dosbox_path="C:\Program Files (x86)\DOSBox-0.74-3\DOSBox.exe"
set dos_dir_path="C:\DOS"
set interpretter_path="C:\conda\envs\convert602\python.exe"
set app_path="C:\Development\Python\C602\app.py"

set command=%interpretter_path% %app_path% %dos_dir_path% %dosbox_path%

%command%