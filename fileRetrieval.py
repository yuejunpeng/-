import os
path = 'D:\Working\毛中特'    # 路径名称
files = os.listdir(path)
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
# 它不包括 . 和 .. 即使它在文件夹中。只支持在 Unix, Windows 下使用。
# python2需要转码：uPath = unicode(path,'utf-8')

for f in files:
    if (f.endswith('.pptx') or f.endswith('.ppt') )and ('第一章' in f or '第二章' in f):
        # endswith()方法 判断字符串是否以指定后缀结尾。
        # and、or、not是python的条件判断符
        print('I found this:'+ f)
    # python可以加括号，如果不加，and优先级高于or。

