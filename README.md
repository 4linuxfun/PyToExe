### 介绍：
Pyinstaller GUI打包工具，方便python项目打包成exe。

### 环境依赖
* python3.8
* wxpython
* pyinstaller

### python解释器
建议选择pythonw.exe，后台执行打包程序，不会有终端显示。如果选择python.exe，则会显示一个终端界面。
### 打包类型：
建议打包成**目录**形式的，启动较快。

### 关于UPX
UPX压缩功能虽然添加了，但是压缩后会启动报错，所以暂时不推荐使用
### 关于加密
加密需要pycrypto库，但是此库长期无人维护。。。所以暂时不添加此功能

### 打包
```
pyinstaller.exe -F -w PyToExe.py -n PyToExe
```
执行完就表示已经创建了一个PyToExe打包程序。