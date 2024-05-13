def task9(n: int) -> None:
    result = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1
    
    while num <= n * n:
        for i in range(left, right+1):
            result[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom+1):
            result[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left-1, -1):
            result[bottom][i] = num
            num += 1
        bottom -= 1
        
        for i in range(bottom, top-1, -1):
            result[i][left] = num
            num += 1
        left += 1
    
    for row in result:
        print(" ".join(map(str, row)))
