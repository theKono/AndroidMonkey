* appium > sample-code > sample-code > examples > node > helpers > caps.js

## caps.js
  * exports.androidxx 用來設定之後抓那一組參數//之後再在simple.js選擇要使用的參數
  * ‘appium-version’:’1.4.16’,//需設定成電腦appium版本， $ appium -v
  * platformVersion: “(uncertain)提醒用, 不影響結果”,
  * deviceName: ‘在Android不影響, (uncertain)iOS需為instruments -s devices所列’, // $instruments -s devices
  * app:’為app的absolute local path或http url，這裡所有的app路徑設定於app.js，再在啟動的檔案(simple.js)選擇要使用的路徑’
  * //_.clone(require(“./helpers/caps”).androidApiDemos);

## android-simple.js
  * require(“./path name”) //pathname： ’檔案不需加.js，加了也可以’，此處需引用caps.js, apps.js，另wd, underscore為套件引用時前面不加./
  * http://dreamerslab.com/blog/tw/node-js-basics/
  * .clone()即複製。
  * line 21 / line 22 判斷要使用caps.js中的那組參數，因為是false所以會有影響的是line22
  * line 23 選擇apps.js中要跑的app

process.env.SAUCE應該是受helpers/appium-server.js影響
