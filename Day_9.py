# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self,node,data):
#         if node is None:
#             return Node(data)
#         if data < node.data:
#             node.left= self.insert(node.left,data)
#         elif data > node.data:
#             node.right = self.insert(node.right,data)
#         return node
#
#     def inorder(self,root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         print(root.data)
#         self.inorder(root.right)
#
# tree=BST()
#
# tree.root=tree.insert(tree.root,20)
# tree.root=tree.insert(tree.root,30)
# tree.root=tree.insert(tree.root,40)
# tree.root=tree.insert(tree.root,60)
#
# tree.inorder(tree.root)
#
#
#
#
# #-----------------------Hacker rank-----------level sum
# class Node:
#     def __init__(self, info):
#         self.info = info
#         self.left = None
#         self.right = None
#         self.level = None
#
#     def __str__(self):
#         return str(self.info)
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def create(self, val):
#         if self.root == None:
#             self.root = Node(val)
#         else:
#             current = self.root
#
#             while True:
#                 if val < current.info:
#                     if current.left:
#                         current = current.left
#                     else:
#                         current.left = Node(val)
#                         break
#                 elif val > current.info:
#                     if current.right:
#                         current = current.right
#                     else:
#                         current.right = Node(val)
#                         break
#                 else:
#                     break
#
#--------https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true
# """
# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)
# """
#
#
# def levelOrder(root):
#     # Write your code here
#     q = []
#     q.append(root)
#     while q:
#         ele = q.pop(0)
#         print(ele, end=" ")
#         if ele.left:
#             q.append(ele.left)
#         if ele.right:
#             q.append(ele.right)
#
#
# tree = BinarySearchTree()
# t = int(input())
#
# arr = list(map(int, input().split()))
#
# for i in range(t):
#     tree.create(arr[i])
#
# levelOrder(tree.root)


#       leetcode 100,101,112,222,226,257