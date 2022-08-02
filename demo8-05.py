# 读取文本文件
# module = 'r' 只读
# module = 'w' 写入 存在覆盖 不存在新建
# module = 'a' 追加 存在追加末尾 不存在新建
# module = 'r+' 用于读写 文件指针会放在文件的开头
# module = 'w+' 用于读写 存在覆盖 不存在新建
# module = 'a+' 用于读写 存在追加末尾 不存在新建
path = 'data/demo10.txt'
# f = open(path, encoding='utf-8')
# txt = f.read()
# print(txt)
# f.close()
# print(' =' * 3)

# f = open(path, 'r')
# while True:
#     line = f.readline()  # 可以带参数指定读取字节数
#     if not line: break
#     print(line, end='')
# f.close()
# print('\n' + ' =' * 30)

f = open(path, 'r')
lines = f.readlines()  # 全部读取结果存在列表中
print(lines)
f.close()
