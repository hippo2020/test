'''
Date: 2023-03-22 20:21:12
LastEditors: jhao
LastEditTime: 2023-03-22 20:35:17
FilePath: \python\p1.py
'''
while 1:
    try:
        n=int(input())
        for i in range(n):
            line=input()
            for i in range(0,len(line),8):
                if len(line[i:i+8])==8:
                    print(line[i:i+8])
                else:
                    #右侧补0
                    print(line[i:i+8].ljust(8,"0"))
    except Exception as e:
        break

