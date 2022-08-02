# with语句文件读操作
# with 用于避免文件打开关闭操作
path = './data/demo10.txt'
with open(path, 'r') as f:
    txt = f.read()
    print(txt)
print(' =' * 30)

with open(path, 'r') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)
print(' =' * 30)

with open(path, 'r') as f:
    lines = f.readlines()
    print(lines)
print(' =' * 30)
