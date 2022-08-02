# 批量修改文件扩展名
import os
path = input('请输入路径：')
zhiqian = input('请输入要修改的扩展名：')
zhihou = input('请输入修改后的扩展名：')
files = os.listdir(path)
for filename in files:
    portion = os.path.splitext(filename)
    if portion[1] == zhiqian:
        newname = portion[0] + zhihou
        os.chdir(path)
        os.rename(filename,newname)
        print(filename,'更改为：',newname)