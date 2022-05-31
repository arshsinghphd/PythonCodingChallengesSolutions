import numpy as np
n=3
raw_arr="11 2 4\n4 5 6\n10 8 -12"
arr = []
arr.append(list(map(int, raw_arr.rstrip().split())))
arr=arr[0]

def diagonalDifference(arr):
    mat=np.zeros((3,3))
    c=0
    for i in range(0,n):
        for j in range(0,n):
            mat[i][j]=arr[c]
            c+=1
    sd1=0
    for i in range(0,n):
        sd1+=mat[i][i]

    sd2=0
    for i in range(0,n):
        sd2+=mat[i][n-1-i]
    
    #print(mat)
    #print(sd1, sd2)
    diff=abs(sd1-sd2)
    return diff

ans=diagonalDifference(arr)
print(ans)
