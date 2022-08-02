# 批量，添加或批量删除文件的前缀
import os

print('功能列表\n'
      '1.批量添加\n'
      '2.批量删除')
sn = int(input('请输入功能序号:'))
prefix = input('请输入前缀:')
path = input('请输入路径:')
flist = os.listdir(path)
print(flist)
for f in flist:
    opj = os.path.join(path, f)
    print(opj)
    if not os.path.isfile(opj):
        continue
    if sn == 1:
        os.rename(opj, os.path.join(path, prefix + f))
    elif sn == 2:
        if f.startswith(prefix):
            os.rename(opj, os.path.join(path, f[len(prefix):]))
        else:
            print('请输入正确的序号')
    else:
        print('执行完成')
