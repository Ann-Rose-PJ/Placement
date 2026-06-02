#  ------------------Reverse------
#  k=int(input())
# rev=0
# while k:
#     f=k%10
#     rev=rev*10+f
#     k=k//10
# print(rev)

#------------------Armstrong----------
# n=int(input())
# arm=0
# temp=n
#
# while n:
#     p=n%10
#     arm=arm+p**3
#     n=n//10
# if temp==arm:
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#-------------   21342-------------

# w=int(input())
# temp=w
# sum=0
# cnt=0
#
# while w:
#     o=w%10
#     cnt=cnt+1
#     w=w//10
#
# u=temp
# i=1
# while u:
#     h=u%10
#     sum=sum+h**i
#     i=i+1
#     u=u//10
# print(sum)


#-----------------Reverse the above------------

# w=int(input())
# temp=w
# sum=0
# cnt=0
#
# while w:
#     o=w%10
#     cnt=cnt+1
#     w=w//10
#
# u=temp
# i=cnt
# while u:
#     h=u%10
#     sum=sum+h**i
#     i=i-1
#     u=u//10
# print(sum)


## ------- Leetcode 1560 A---------------------------
# g=int(input())
# for i in range(g):
#     n=int(input())
#     i=0
#     k=1
#     while 1:
#         if i%3!=0 and i%10!=3:
#             if n==k:
#                 print(i)
#                 break;
#             k=k+1
#         i=i+1


####--------------------prime---------------------

z=int(input())

flag=0
for i in range(2,int(z**.5)+1):
    if z%i==0:
        flag=1
        break
if flag==0:
    print("Prime")
else:
    print("Composite")



####-------------------Duplicate value-------------------
# l=list(map(int,input().split()))
# l2=[]
# for i in l:
#     if i not in l2:
#         l2.append(i)
# print(l2)
#


##############------------------Odd num of times occured-------------------

# l=list(map(int,input().split()))
# l2=[]
# for i in l:
#     if i not in l2 and l.count(i)%2!=0:
#         l2.append(i)
# print(l2)

##--------------------------Sort and put even odd--------------

l2=list(map(int,input().split()))
res=[]
l2.sort()
for i in l2:
    if i%2!=0:
        res.append(i)
    else:
        res.insert(0,i)
print(res)


