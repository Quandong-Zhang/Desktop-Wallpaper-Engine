import ctypes
import time
import os
cln=1
shijian=0.19
path=os.getcwd()
while True:
  paths=path+".\pic\image"+str(cln)+".jpg"
  if os.path.exists(paths):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, paths, 0)  # 设置桌面
    time.sleep(shijian)
    cln+=1
  else:
    cln=1