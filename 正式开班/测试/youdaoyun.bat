@echo off

adb connect 127.0.0.1:7555
adb shell am start -n com.youdao.note/.activity2.MainActivity
TIMEOUT /T 2
adb shell input tap 359 1243
TIMEOUT /T 2
adb shell input tap 92 1188
TIMEOUT /T 3
adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'Test Content'
TIMEOUT /T 3
adb shell input tap 62 162
TIMEOUT /T 3
adb shell am broadcast -a ADB_INPUT_TEXT --es msg 'Test Title'
TIMEOUT /T 2
adb shell screencap -p /sdcard/sc.png
TIMEOUT /T 3
adb shell input tap 664 83
TIMEOUT /T 3
adb pull sdcard/sc.png
pause