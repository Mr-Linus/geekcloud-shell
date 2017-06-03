import psutil,datetime,os
def memory():
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        print("-----内存使用情况-----")
        print("当前内存: "+str(int(mem.total/1024/1024))+"M")
        print("已使用内存: "+str(int(mem.used/1024/1024))+"M")
        print("空闲内存: "+str(int(mem.free/1024/1024))+"M")
        print("-----SWAP使用情况-----")
        print("当前SWAP: "+str(int(swap.total/1024/1024))+"M")
        print("空闲SWAP: "+str(int(swap.free/1024/1024))+"M")
def cpu():
	cpu = psutil.cpu_times()
	print("CPU核心数:"+str(psutil.cpu_count(logical=False)))
	print("CPU线程数:"+str(psutil.cpu_count()))
def disk():
        def optback(opt):
            if (opt == 'ro'): return ("只读")
            elif (opt == 'rw'): return ("读写")
            else : return ("未知")
        disk = psutil.disk_partitions()
        print("-----设备信息-----")
        for i in range(0,len(disk)):
           print ("设备名:"+str(disk[i].device),end=' ')
           print ("挂载点:"+str(disk[i].mountpoint),end = ' ')
           print ("文件系统:"+str(disk[i].fstype),end = ' ')
           print ("权限:"+optback(disk[i].opts))
def ip():
        ip = psutil.users()
        print("IP:"+str(ip[0].host))
def times():
        uptime = datetime.datetime.fromtimestamp(psutil.boot_time())
        nowtime = datetime.datetime.now()
        print ("当前时间: "+str(nowtime.strftime("%Y-%m-%d %H:%M:%S")))
        print ("服务器已运行: "+str('%.2f' % ((uptime-nowtime).seconds/3600))+"小时")
def install():
         app = input("输入安装的应用名:")
         info  = os.popen("yum install -y %s  " % app )
         print(info.read())
def run():
         command = input("请输入你要执行的命令:")
         info = os.popen(command)
         print("-----执行结果----")
         print(info.read())
