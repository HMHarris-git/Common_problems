
'''
Clockwise and Anti-clockwise 2D List traversal
'''

def list_input():
    '''
    Returns a 2D array of size n*n 
    '''
    size = int(input("Enter size of list."))
    data = []
    while size > 0:
        data.append(list(map(int, input().split())))

        size -= 1

    return data    

def clockwise_spiral_traversal(Arr):
    '''
    Returns a flattened list of elements in clockwise spiral.
    '''
    size = len(Arr)
    Result = []
    direc = 0 
    '''
    direc sets the direction of traversal 
    0 for Right 
    1 for Down
    2 for Left
    3 for Up
    '''
    Top = Left = 0
    Bottom = Right = size-1
    while Left <= Right and Top <= Bottom:

        if direc == 0:
            for ind in range (Left, Right+1):
                Result.append(Arr[Top][ind])
            Top += 1

        if direc == 1:
            for ind in range (Top, Bottom+1):
                Result.append(Arr[ind][Right])
            Right -= 1

        if direc == 2:
            for ind in range (Right, Left-1, -1):
                Result.append(Arr[Bottom][ind])
            Bottom -= 1

        if direc == 3:
            for ind in range (Bottom, Top-1, -1):
                Result.append(Arr[ind][Left])
            Left += 1                
            
        direc = (direc + 1) % 4

    return Result

def matrix_transpose(Arr):
    '''
    Returns transpose of given matrix
    '''
    Result = [[None for j in range(len(Arr[0]))] for i in range (len(Arr))]
    for i in range(len(Arr)):
        for j in range(len(Arr[0])):
            Result[j][i] = Arr[i][j] 

    return Result        

def anti_clockwise_spiral_traversal(Arr):
    '''
    Returns a flattened list of elements in anti-clockwise spiral.
    A anti-clockwise spiral traversal is basically clockwise traversal of transpose of original array.
    '''
    ArrT = matrix_transpose(Arr) # Generating transpose of given matrix

    return clockwise_spiral_traversal(ArrT)


if __name__ == "__main__" :

    # print(list_input())

    Arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    print(Arr)
    print(clockwise_spiral_traversal(Arr))
    print(anti_clockwise_spiral_traversal(Arr))