# 读取多个文件的内容
import fileinput
lst = ['/data/demo10.txt','/data/abc.txt']
for line in fileinput.input(lst):
    print(line, end='')
