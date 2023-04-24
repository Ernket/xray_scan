# 作用
使用python3调用高级版xray多线程扫描，方便大批量扫描，同时还加上了进度条功能，方便查看当前扫描进度

# 环境
- 编写环境：python3.9.7

# 用法
将`xray.exe`和`rad.exe`放置在同目录下，然后新建`url.txt`，在里面写入自己扫描的url，接着运行
```
python3 xray_scan.py
```
你也可以手动设置线程数，默认为3
```
python3 xray_scan.py -t 2
```
