import ctypes
import time
import os
cln=0
shijian=0.19
path=os.getcwd()
while True:
  cln+=1
  paths=path+".\pic\image"+str(cln)+".jpg"
  time.sleep(shijian)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, paths, 0)  # 设置桌面