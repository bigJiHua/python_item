# 案例3删除文件
import sys
import os
import shutil


def fileDir():  # 获取文件路径
    path = input('输入文件路径：')
    print(path)
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def suffix(file, *suffix):  # 获取文件扩展名
    array = map(file.endswith, suffix)
    if True in array:
        return True
    else:
        return False


def deleteFile():
    targetDir = fileDir()
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        if suffix(file, '.tmp', '.log'):
            os.remove(targetFile)
            print(file + '文件已删除')


deleteFile()
