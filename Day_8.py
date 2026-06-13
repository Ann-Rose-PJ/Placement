
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# head=Node(10)
# head.next= Node(20)
# head.next.next= Node(30)
# head.next.next.next= Node(40)
# head.next.next.next.next= Node(50)
#
# temp=head
# while temp:
#     print(temp.data,end=" ")
#     temp=temp.next
#
# print(None)

#-----------------------------------------------------------------------

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data,end="->")
#             temp = temp.next
#         print(None)
#     def count(self):
#         cnt=0
#         temp = self.head
#         while temp:
#             cnt+=1
#             temp = temp.next
#         print(cnt)
#
#     def even(self):
#         temp = self.head
#         sum=0
#         while temp:
#             if temp.data%2==0:
#                 sum+=temp.data
#             temp=temp.next
#         print(sum)
#
# l1=LinkedList()
# l1.append(2)
# l1.append(15)
# l1.append(20)
# l1.append(30)
# l1.append(40)
# l1.append(50)
#
#
# l1.display()
# l1.even()
# l1.count()

#------------------------------------------- leetcode 876------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         temp = head
#         cnt = 0
#         while temp:
#             cnt += 1
#             temp = temp.next
#         temp2 = head
#         y = cnt // 2
#         for i in range(y):
#             temp2 = temp2.next
#         return temp2



#------------------------------------leetcode  206-----------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

#------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

