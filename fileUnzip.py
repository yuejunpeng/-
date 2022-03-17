import os
import shutil

def scan_file():
    for f in os.listdir():          # 默认为当前路径
        if f.endswith('.zip'):
            return f

def unzip_it(f):
    folder_name = f.split('.')[0]   # 表示第一个.之前的内容
    target_path = './' + folder_name
    os.makedirs(target_path)
    shutil.unpack_archive(f,target_path)

def delete(f):
    os.remove(f)

# while true的意义是将文件夹中的所有压缩文件都解压，否则只解压一个
while True:
    zip_file = scan_file()
    if zip_file:
        unzip_it(zip_file)
        delete(zip_file)


# zip_file = scan_file()
# if zip_file:
#     unzip_it(zip_file)
#     delete(zip_file)