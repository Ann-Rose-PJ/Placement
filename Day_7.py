#----------------Monotonic-----------------------------

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        st=[]
        for curr in nums2:
            while st and st[-1]<curr:
                ele=st.pop()
                d[ele]=curr
            st.append(curr)
        while st:
            d[st.pop()]=-1
        res=[]
        for i in nums1:
            res.append(d[i])
        return res

#-------------------------------------------------

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


#---------------------------------------------------------------------------

class Solution:
    def makeGood(self, s: str) -> str:
        st = []

        for i in s:
            if st and st[-1] != i and st[-1].lower() == i.lower():
                st.pop()
            else:
                st.append(i)

        return ''.join(st)

#--------------------------------------------------------------------------------------
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        while students and sandwiches and sandwiches[0] in students:
            if students[0]!=sandwiches[0]:
                students.append(students.pop(0))
            else:
                n-=1
                students.pop(0)
                sandwiches.pop(0)
        return n


#----------------------------------------------------------------------