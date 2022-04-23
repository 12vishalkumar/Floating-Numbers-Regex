import re
T = int(input())
for i in range(T):
    ft = input()
    try:
        num = float(ft)
        print('.' in ft)
    except ValueError:
        print(False)