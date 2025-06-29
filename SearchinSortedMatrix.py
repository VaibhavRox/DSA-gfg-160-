def searchMatrix(mat, x):
    n = len(mat)
    m = len(mat[0])
    low, high = 0, n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if mat[row][col] == x:
            return True
        elif mat[row][col] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False
