import ctypes
import time
import os
cln=0
shijian=0.19
lujing=os.getcwd()
while True:
  cln=cln+1
  spf=lujing+"\spf\image"+str(cln)+".jpg"
  time.sleep(shijian)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, spf, 0)  # 设置桌面
