import math

def flip_matrix_and_sum(matrix):
    # Flatten out the matrix first
    flattened = [element for row in matrix for element in row]

    # Sort in descending order
    flattened.sort(reverse=True)

    #Rebuild the matrix with the largest values concentrated in the upper-left quadrant.
    rows = len(matrix) 
    cols = int(math.sqrt(len(flattened)))

    new_matrix = [flattened[i:i+cols] for i in range(0,len(flattened), cols)]

    #Define quadrant
    half_rows = rows // 2
    half_cols = cols // 2

    #Sum the elements in the upper-left quardant
    quadrant_sum = 0
    for i in range(half_rows):
        for j in range(half_cols):
            quadrant_sum += new_matrix[i][j]
            
    return quadrant_sum
