###---------------left -Rotate with o(n)--------------------

# li3=list(map(int,input().split()))
#
# n=len(li3)
# k=int(input())
# k=k%n
# def rever(i,j):
#     while i<j:
#         li3[i],li3[j]=li3[j],li3[i]
#         i+=1
#         j-=1
#
# rever(0,k-1)
# rever(k,n-1)
# rever(0,n-1)
# print(li3)


###------------right rotate    o(n)-------------

# li3=list(map(int,input().split()))
#
# n=len(li3)
# k=int(input())
# k=k%n
# def rever(i,j):
#     while i<j:
#         li3[i],li3[j]=li3[j],li3[i]
#         i+=1
#         j-=1
#
# rever(0,n-1)
# rever(0,k-1)
# rever(k,n-1)

# print(li3)


#-----------------------------------mergesort--------2 ponters--------
# li1=list(map(int,input().split()))
# li2=list(map(int,input().split()))
# res=[]
# n1=len(li1)
# n2=len(li2)
# n=n1+n2
# i,j=0,0
#
# while i<n1 and j<n2:
#     if li1[i]>li2[j]:
#         res.append(li2[j])
#         j+=1
#     else:
#         res.append(li1[i])
#         i=i+1
#
# while j<n2:
#     res.append(li2[j])
#     j+=1
# while i<n1:
#     res.append(li1[i])
#     i=i+1
# print(res)

#-#-----------------------------------------------------------------------------------

lin=list(map(int,input().split()))
k=int(input())

n=len(lin)
s=sum(lin[:k])
m=s

for i in range(1,n-k+1):

    s=s-lin[i-1]+lin[i+k-1]
    m=max(m,s)

print(m)


#---------------------------Ugly number    -------------------
class Solution:
    def isUgly(self, n: int) -> bool:
        # li1=[2,3,5]
        # for i in range(2,n//2):
        #     k=n%i
        #     if k%i==0:
        #         break
        #     if k not in li1:
        #         return False
        # return True

        if n <= 0:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i
        return n == 1
 ##---------------------------------------------------------

#-----------------------------------------------------

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        m = 0.0
        n = len(nums)
        s = sum(nums[:k])
        m = s

        for i in range(1, n - k + 1):
            s = s - nums[i - 1] + nums[i + k - 1]
            m = max(m, s)

        return m / k



#3###------------------------valid palindrome

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                left = s[i + 1:j + 1]
                right = s[i:j]
                if left == left[::-1] or right == right[::-1]:
                    return True
                else:
                    return False
            i += 1
            j -= 1
        return True






