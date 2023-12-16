sparseMatrix = [[0, 0, 3, 0, 4],
                [0, 0, 5, 7, 0],
                [0, 0, 0, 0, 0],
                [0, 2, 6, 0, 0]]
newarr = []
for i in range(len(sparseMatrix)):
    for j in range(len(sparseMatrix[0])):
        if sparseMatrix[i][j] != 0:
            newarr.append([i,j,sparseMatrix[i][j]])
print(newarr)
