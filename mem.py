import libs
print("-----欢迎使用极云监控系统-----")
print("常用命令:"+'\n'+"  cpu、disk、memory、ip")
print("使用exit命令退出系统!")
while (1) :
  try:
   getinput = input('GeekCloud:>')
   if(str(getinput) == "exit" or str(getinput)== '^C' ): 
      print("退出系统!")
      break
   if(str(getinput) == '' ):
      continue
   command = getattr(libs,getinput)
   command()
  except KeyboardInterrupt:
      print("退出系统!")
      break
  except : print('"'+str(getinput)+'"'+"不存在的命令!")
