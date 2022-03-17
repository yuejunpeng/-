import shutil
import os

path = './'  # ./表示当前目录名
files = os.listdir(path)

for f in files:
    folder_name = './' + f.split('.')[-1]
    # print(folder_name)
    # 只保留最后一部分，即文件后缀名。详见：https://blog.csdn.net/jialibang/article/details/84989279
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f,folder_name)
    else:
        shutil.move(f,folder_name)
