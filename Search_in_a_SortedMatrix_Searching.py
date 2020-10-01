#Time - O(N+M) / Space - O(1)
def search(matrix,key):
    row=0
    col=len(matrix[0])-1
    while row < len(matrix) and col > 0:
        if(key < matrix[row][col]):
            col-=1
        elif(key > matrix[row][col]):
            row+=1
        else:
            return [row,col]
    return [-1,-1]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(search(matrix,9))
