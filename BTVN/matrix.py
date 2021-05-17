x = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
def rotate90(x):
    n = len(x)
    y = [[0 for x in range(n)] for y in range(n)]
    for i in range(n//2):
        for j in range(i,n-i-1):
            y[i][j],y[n-1-j][i],y[n-1-i][n-1-j],y[j][n-1-i] = x[j][n-1-i],x[i][j],x[n-1-j][i],x[n-1-i][n-1-j]
    return y
def rotate180(x):
    n = len(x)
    y = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        y[i] = x[n-1-i][::-1]
    return y
print(x)
print(rotate90(x))
print(x)
print(rotate90(rotate90(x)))
print(rotate180(x))

