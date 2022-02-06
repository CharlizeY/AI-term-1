def recursive_fill(image, seed_point):
    row = seed_point[0]
    col = seed_point[1]

    if (isinstance(row, int) and isinstance(col, int)) == False:
        # print("The seed point has a non-integer coordinate.")
        return image
        
    if row < 0 or row > len(image) - 1 or col < 0 or col > len(image[0]) - 1:
        # print("The seed point is outside the image.") 
        return image
    
    if image[row][col] != 0:
        # print("The seed point is on a boundary pixel.")
        return image
    else:
        image[row][col] = 2

    recursive_fill(image, (row - 1, col))
    recursive_fill(image, (row + 1, col))
    recursive_fill(image, (row, col - 1))
    recursive_fill(image, (row, col + 1))

    return image



