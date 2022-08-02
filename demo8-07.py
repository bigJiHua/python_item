# 掌握文本文件逐行读取
with open('./data/demo10.txt','r') as f:
    for line in f:
        print(line)

print(' =' * 30)
