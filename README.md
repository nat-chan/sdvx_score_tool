#sdvxのスコアツール

全楽曲をハイスコアを次の形式で標準出力に書き出すだけ

楽曲名, アーティスト, EXH, MXM, {INF or GRV or HVN}

```bash
$ python ./gui.py
```

wx.App.MainLoop()が終わってもwebdriverをデストラクトしないようにしたのでipythonとかで
いい感じにできる。

ターミナル上で
```python
import wx
import os
from selenium import webdriver
from gui import ScoreTool
app = wx.App()
driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
frame = ScoreTool(None, driver, -1, title='score_tool')
frame.Show()
app.MainLoop()
```
これで認証済みのwebdriverができる

PhantomJSを[ここ](http://phantomjs.org/download.html)から落として、実行可能ファイルを
環境変数の通ったとこに置いてください。

gui.pyの頭の方にUSERNAMEとPASSWORD書くところがあるから埋めとくと勝手に入る
