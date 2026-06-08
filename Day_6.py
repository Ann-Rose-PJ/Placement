##### --------------5 4 3 2 1----------------
# def rev(n):
#     if n == 0:
#         return 0
#     print(n)
#     rev(n-1)
#
# n=5
# rev(n)
#
# # #---------------1 2 3 4 5-------
#
#
#def rev(n):
#     if n == 0:
#         return 0
#
#     rev(n-1)
#     print(n)
# n=5
# rev(n)


# ------------- 10 8 6 4 2------
# def rev(n):
#     if n==0:
#         return
#     print(n)
#     rev(n-2)
# n=10
# rev(n)


#--------------2 4 6 8 10----------
# def rev(n):
#     if n==0:
#         return
#
#     rev(n-2)
#     print(n)
# n=10
# rev(n)

#------------------------------
# def rev(n):
#     u=200
#     if n == 0 :
#         return 200
#     t=rev(n-1)
#     print(n ,end=" ")
#     return t
#
# n=5
# print(rev(n))

#----------------5 4 3 2 1 1 2 3 4 5-------
# def rev(n):
#     if n == 0:
#         return 0
#     print(n,end=" ")
#     rev(n-1)
#     print(n,end=" ")
# n=5
# rev(n)

#---------------10 8 6 4 2 4 6 10---------
# def rev(n):
#     if n == 0:
#         return 0
#     if n%2==0:
#         print(n, end=" ")
#     rev(n-1)
#     if n%2==0 and n>3:
#         print(n, end=" ")
# n=10
# rev(n)

##---------------1 2 3 4 5 4 3 2 1----------------------------------------------------

# def fum(n,m=0):
#     if n==m:
#         return
#     print(m+1,end=" ")
#     fum(n,m+1)
#     if n:
#         print(m+1, end=" ")
#
# n=5
# fum(n)

#------------------divide in easy------
# def check(n):
#     if n==1:
#         return 0
#
#     elif n%2==0:
#         return 1+check(n//2)
#     else:
#         return 1+min(check(n-1),check(n+1))
#
#
# n=int(input())
#
# print(check(n))



#-------------------------Tree Recursion

# def wildfire(grid,i,j):
#     if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
#         return
#     grid[i][j]=2
#     wildfire(grid,i+1,j)
#     wildfire(grid,i-1,j)
#     wildfire(grid,i,j+1)
#     wildfire(grid,i,j-1)
#
#
#
# matrix=[[1,1,1,1],
#         [1,0,0,0],
#         [0,0,1,1],
#         [0,1,0,0]]
#
# wildfire(matrix,0,0)
# count=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==1:
#             count+=1
# print(count)


#-------------------robot down and right------------

def maze(grid,path,i,j,n):
    if i==n and j==n:
        print(path)
        return
    if i+1<=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j,n)
    if j+1<=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1,n)

grid=[[1,1,0,1],
     [1,1,0,1],
     [0,1,0,0],
     [1,1,1,1]]

n=len(grid)
maze(grid," ",0,0,n-1)
