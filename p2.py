'''
Date: 2023-03-23 19:44:17
LastEditors: jhao
LastEditTime: 2023-03-23 19:49:38
FilePath: \python\p2.py
'''
while 1:
    try:
        n=int(input())
        temp=[]
        for i in range(n):
            temp += list(map(int,input().split()))

        total=sum(temp)
        print(total)
    except Exception:
        break 
    