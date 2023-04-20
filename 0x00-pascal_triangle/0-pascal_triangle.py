def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate the remaining rows of the triangle
    for i in range(1, n):
        # Initialize the current row with the first element
        row = [1]
        
        # Generate the middle elements of the row
        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        
        # Append the last element to the row
        row.append(1)
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle

