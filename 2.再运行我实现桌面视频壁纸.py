import ctypes
import time
import os
pic_num=1
times=0.19
path=os.getcwd()
while True:
  paths=path+".\pic\image"+str(pic_num)+".jpg"
  if os.path.exists(paths):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, paths, 0)  # 设置桌面
    time.sleep(times)
    pic_num+=1
  else:
    pic_num=1