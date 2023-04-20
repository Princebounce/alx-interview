def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1] * (i + 1)

        for j in range(1, i):
            curr_row[j] = prev_row[j - 1] + prev_row[j]

        triangle.append(curr_row)

    return triangle

