def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    max_sum = 0
    for i in range(n // 2):
        for j in range(n // 2):
            top_left = matrix[i][j]
            top_right = matrix[i][n - j - 1]
            bottom_left = matrix[n - i - 1][j]
            bottom_right = matrix[n - i - 1][n - j - 1]
            max_value = max(top_left, top_right, bottom_left, bottom_right)
            max_sum += max_value
    return max_sum
