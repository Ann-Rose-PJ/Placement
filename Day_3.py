######--------------------Leetcode 66-----------------
from itertools import count

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits
#         return [1] + digits

######--------------------------------power of 2------------------
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n < 1:
#             return False
#         while (n):
#             if n == 1:
#                 return True
#             elif n % 2 != 0:
#                 return False
#             else:
#                 n = n // 2


#-----OR-----
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n<1:
#             return False
#         if n &(n-1)==0:
#                 return True
#         else:
#                 return False

#-------------------------2nd largest element

# l=list(map(int,input().split()))
# max=0
# for i in l:
#     if i>max:
#         p=max
#         max=i
#     elif i>p and i!=max:
#         p=i
#
# print(p)


####-------------------------fequency count------------------------------
# l=list(map(int,input().split()))
# d={}
# for i in l:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# ele,maz=0,0
# for i in d:
#     if d[i]>maz:
#         maz=d[i]
#         ele=i
#     elif d[i] > maz and i != maz:
#         maz=i


##-------------------------------Counting votes--------------
# j=int(input())
# vote=list(map(int,input().split()))
# age=list(map(int,input().split()))
# c=[0]*max(vote)
# #d={}
# for i in  range(j):
#     if age[i]>=18:
#         c[vote[i]-1]+=1
# m=max(c)
# print(c.index(m)+1)
# temp=sorted(c,reverse=True)
# if temp[0]==temp[1]:
#     print(-1)
# else:
#     print(c.index(temp[0])-1)
#
# ##      output------
# # 5
# # 1 2 1 3 2
# # 17 21 20 19 18 17
#
#

#----------------------Reverse a list------without fn

# li=list(map(int,input().split()))
# o=len(li)
# for i in range(o//2):
#     temp=li[i]
#     li[i]=li[o-1]
#     li[o-1]=temp
#     o=o-1
# print(li)


#--------------- left   Rotate-------------------

# li1=list(map(int,input().split()))
# n=len(li1)
# temp=li1[0]
# for i in range(0, n - 1):
#     li1[i] = li1[i + 1]
# li1[n - 1] = temp
#
# print(li1)

###----------------left rotate 2 times-----------
li1=list(map(int,input().split()))
n=len(li1)
k=2
while(k>0):
    temp=li1[0]
    for i in range(0, n - 1):
        li1[i] = li1[i + 1]
    li1[n - 1] = temp
    k=k-1
print(li1)

###---------------Right rotate-------------------------
# li1 = list(map(int, input().split()))
# n = len(li1)
# temp = li1[-1]
# for i in range(n-1,0,-1):
#     li1[i] = li1[i - 1]
# li1[0] = temp
# print(li1)
















