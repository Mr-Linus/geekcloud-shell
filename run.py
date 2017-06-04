import libs
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import WordCompleter
print("""-----欢迎使用极云监控系统-----
 常用命令:
 cpu、disk、memory、ip
 使用exit命令退出系统!""")
Completer = WordCompleter(['cpu', 'disk', 'scan', 'ip', 'memory', 'times','exit','install','run'],
                             ignore_case=True)
while (1) :
  try:
   getinput = prompt('GeekCloud:>',history=FileHistory('history.txt'),auto_suggest=AutoSuggestFromHistory(),completer=Completer,)
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
