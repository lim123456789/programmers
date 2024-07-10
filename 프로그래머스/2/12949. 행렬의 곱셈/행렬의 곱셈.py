def solution(arr1, arr2):

    rows = len(arr1)
    cols = len(arr2[0])
    
    result = [[0] * cols for i in range(rows)]
    
    for x in range(rows):
        for y in range(cols):
            for z in range(len(arr2)):
                result[x][y] += arr1[x][z] * arr2[z][y]
    
    return result