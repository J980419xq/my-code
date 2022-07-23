
n=256
'''n=str(n)
n=[int(i) for i in n]
'''
n=list(map(int,list(str(n))))
print(n[-1::-1])