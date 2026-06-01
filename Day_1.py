###########-------
#https://codeforces.com/problemset/problem/617/A

l=int(input())
if l<5:
    print(1)
elif l%5==0:
    print(l//5)
else:
    print(l//5+1)


#####-------4 a
#https://codeforces.com/problemset/problem/4/A

p=int(input())
if p%2!=0 or p==2:
    print("No")
else:
    print("Yes")
    if p%2==0:
        print()


# Bear

a,b=map(int,input().split())
cnt=0
while a<=b:
    cnt+=1
    a=a*3
    b=b*2
print(cnt)


###################------Cheap Travel

n,m,a,b=map(int,input().split())

if a*m<b:
    print(a*n)
else:
    print(((n//m)*b)+min(b,(n%m)*a))

