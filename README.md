# 极云终端 

基于Python3开发的终端系统
目前支持的命令:
```shell 
    cpu  查看cpu核心数
    disk 查看磁盘情况
    scan 扫描固定IP端口
    ip 查看ip
    memory 查看内存使用情况
    times 查看主机开启时间
    install 使用YUM安装程序
    run  运行shell命令
```
## 效果
![alt](https://github.com/Mr-Linus/geekcloud-shell/blob/master/screen.gif)
## 更新 V0.1
支持历史记录,支持自动补全
## python依赖包
```shell
    pip install prompt_toolkit
    pip install threadpool 
    pip install psutil 
```
## 运行程序
```shell
    python ./terminal-py/run.py
```
