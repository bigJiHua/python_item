# 使用 fileinput 给源代码行末添加注释及括号
import fileinput

for line in fileinput.input('demo8-09.py', inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print(' {:<60} # {:2d}'.format(line, num))
