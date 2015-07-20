# AndroidMonkey
This repository contains the test script for Kono Android app.

# Setup
## ADB
* 裝好 ADB，加到環境變數
* 打開 '開發人員選項' ：設定 -> 關於手機 -> 軟體版本，連續點 '軟體版本' 直到打開
* 點選 '開發人員選項' -> 開啓 'USB 偵錯'
* 測試電腦有抓到手機：`adb devices`
* 延伸閱讀：http://developer.android.com/tools/help/adb.html

## Monkey Runner
* 把 androidSDK/tools/monkeyrunner 加到環境變數
* 就這樣

# Monkey Test
* 用來做壓力測試
* ex: `adb shell monkey -p com.kono.reader.test -v 500`
  * `com.kono.reader.test` ：Kono 測試版專用的 package name
* 參考：http://developer.android.com/tools/help/monkey.html
  * (?) --pct-trackball: app 常常需要 user 滑動後 click
  * (?) --throttle: app 常會用到網路，可設 1 秒左右

# Monkey runner
* 寫 code 跑重覆點擊的測試，這個 repository 放 code 的應該都是這類
* Using Python
* Launch script: `monkeyrunner mymonkey.py`
* 參考：http://developer.android.com/tools/help/monkeyrunner_concepts.html

# Contribute
1. Fork this repo
2. Add test cases or fix bugs
3. [Create a pull request](https://help.github.com/articles/creating-a-pull-request/)
