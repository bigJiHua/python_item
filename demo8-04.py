import os
for p, d, f in os.walk('.'):
    print('--------------------------')
    print(p,'=>', os.path.abspath(p))
    print(d)
    print(f)
    print('--------------------------\n')