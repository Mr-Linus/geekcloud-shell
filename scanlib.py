import threadpool,time
from  socket import *
balance = 0
def scan():
   def portScanner(port):
       try:
           s = socket(AF_INET,SOCK_STREAM)
           s.connect((ip,port))
           print('[+] %d 开启' % port)
           s.close()
       except: pass
   ip = input("IP:")
   sPort = int(input('Start:'))
   ePort = int(input('End:'))
   ePort += 1
   print("开始扫描:")
   start_time=time.time()
   pool=threadpool.ThreadPool(10)
   reqs=threadpool.makeRequests(portScanner,[x for x in range(sPort,ePort)])
   [pool.putRequest(x) for x in reqs]
   pool.wait()
   print('扫描完毕!')
   print("用时：{}秒".format(time.time()-start_time))
