import os


# level:递归的层数,该参数用于控制打印的缩进
# #path:遍历指定的路径
def fileTree(level, path):
    for f in os.listdir(path):
        print(' -' * (level + 1) + f)
        if os.path.isdir(path + ' \\' + f):
            fileTree(level + 1, path + ' \\' + f)


# 打印当前绝对路径
rootpath = os.path.abspath('.')
print(rootpath)

# 调用递归函数
fileTree(0, rootpath)
