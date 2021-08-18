# Two-dimensional lists
a = [[1, 2, 3],[4, 5, 6]]
'''       a
column 0  1  2
row 0 [1  2  3] 
    1 [4  5  6]
'''
# print(a[1][1])
# print(a[0])
# b = a[1]
# print(b)

# a[0][1] = 7
# print(a[0][1])
#
#print(a)

# แสดงผล

for row in a:
     print(' '.join([str(elem) for elem in row]))


# สร้าง
# b = [[0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]]

# m = 3 #column
# n = 3 #row
# b = [[0] * m for i in range(n)]
#
# for row in b:
#     for elem in row:
#         print(elem, end=' ')
#     print()


# รับค่า
n = int(input())
c = []

c = [[int(j) for j in input().split()] for i in range(n)]
#
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