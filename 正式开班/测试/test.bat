@echo off

adb device
adb shell am start -a android.intent.action.VIEW -d  https://www.baidu.com
TIMEOUT /T 3
adb shell input text bilibili
TIMEOUT /T 3
adb shell input tap 859 176
TIMEOUT /T 3
adb shell input tap 354 320

adb shell am start -n com.youdao.note/.activity2.MainActivity

adb shell dumpsys activity activities | findstr "mFocusedActivity"
adb shell am start -n activity有名
adb shell input swipe startX startY endX endY 500  滑动
pause