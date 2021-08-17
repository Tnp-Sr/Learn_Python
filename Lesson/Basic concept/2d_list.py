# Two-dimensional lists
a = [[1, 2, 3],[4, 5, 6]]
'''       a
column 0  1  2
row 0 [1  2  3] 
    1 [4  5  6]
'''
# print(a[0][1])
# print(a[0])
# b = a[1]
# print(b)

# a[0][1] = 7
# print(a[0][1])
#
# print(a)

# แสดงผล
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# for row in a:
#     print(' '.join([str(elem) for elem in row]))


# สร้าง
m = 3 #column
n = 3 #row
b = [[0] * m for i in range(n)]  

# for row in b:
#     for elem in row:
#         print(elem, end=' ')
#     print()


# รับค่า
n = int(input())
c = []

# for i in range(n):
#     c.append([int(j) for j in input().split()])

#  c = [[int(j) for j in input().split()] for i in range(n)]

# for row in c:
#     for elem in row:
#         print(elem, end=' ')
#     print()

'''   
3
2 5 4
2 6
5 9 8 7
'''