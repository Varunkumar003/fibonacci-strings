k,m=map(int,input().split())
l=[]
for i in range(0,5):
    p=input()
    l.append(p)
f1='a'
f2='b'
f3=''
for i in range(0,k-2):
    f3=f2+f1
    f1=f2
    f2=f3
for i in l:
    c=f3.count(i)
    print(c)
