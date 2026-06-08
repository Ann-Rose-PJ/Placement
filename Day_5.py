#----------------subarray with length greatest------sum lessthan or equal to k-----

# li1=list(map(int,input().split()))
# l,r,s=0,0,0
# k=int(input())
# m=0
# while r<len(li1):
#     s+=li1[r]
#     while s>k :
#         s-=li1[l]
#         l+=1
#     length=r-l+1
#
#     m=max(m,length)
#
#     r+=1
# print(m)

#------------------------------password-------------


# s=input()
# upper=False
# digit=False
# space=False
# special=False
# lower=False
#
# for i in s:
#     if i.isdigit():
#         digit=True
#     elif i.isupper():
#         upper=True
#     elif i.islower():
#         lower=True
#     elif i.isspace():
#         space=True
#     else:
#         special=True
#
# if len(s)>=8 and digit==True and space==False and lower==True and upper==True and special==True:
#     print("Valid")
# else:
#     print("Invalid")
#

#----------------------variety--------------------------
sr=input()
che=""
cnt=1
j=0
for i in range(0,len(sr)-1):
    if sr[i]==sr[i+1]:
        cnt+=1

    else:
        che+=sr[i-1]+str(cnt)
        cnt=1
che+=sr[i]+str(cnt)
print(che)








