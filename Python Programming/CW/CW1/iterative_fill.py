import copy
import random

def is_unfilled(image, row, col):
    '''
    Check whether a pixel has label 0.
    '''
    if (row < 0 or row > len(image) - 1):
        return False

    if (col < 0 or col > len(image[0]) - 1):
        return False

    if image[row][col] == 0:
        return True
    else:
        return False


def fill(image, seed_point):
    '''
    Iterative version of bucket fill algorithm. Works better for larger images.
    '''
    row = seed_point[0]
    col = seed_point[1]
    filled_image = copy.deepcopy(image)
    
    if (isinstance(row, int) and isinstance(col, int)) == False:
        # print("The seed point has a non-integer coordinate.")
        return filled_image

    if (row < 0 or col < 0):
        # print("The seed point has a negative coordinate.")
        return filled_image

    if (row > len(image) - 1 or col > len(image[0]) - 1):
        # print("The seed point is outside the image.")
        return filled_image
    
    if filled_image[row][col] == 1:
        # print("The seed point is on a boundary pixel.") 
        return filled_image

    p = []  # Initiate an empty list of points
    filled_image[row][col] = 2  # Mark the seed point as filled
    p.append((row, col))  # Add the seed point to the list

    while len(p) > 0:
        (cur_row, cur_col) = p[0]
        del p[0] # To make sure new points are always explored

        if is_unfilled(filled_image, cur_row - 1, cur_col):
            filled_image[cur_row - 1][cur_col] = 2
            p.append((cur_row - 1, cur_col))

        if is_unfilled(filled_image, cur_row + 1, cur_col):
            filled_image[cur_row + 1][cur_col] = 2
            p.append((cur_row + 1, cur_col))

        if is_unfilled(filled_image, cur_row, cur_col - 1):
            filled_image[cur_row][cur_col - 1] = 2
            p.append((cur_row, cur_col - 1))

        if is_unfilled(filled_image, cur_row, cur_col + 1):
            filled_image[cur_row][cur_col + 1] = 2
            p.append((cur_row, cur_col + 1))

    return filled_image



## Testing
# Test for 1*1 images
def test_one_pixel():
    pixel_1 = [[0]]
    pixel_2 = [[1]]
    seed_point = (0,0)
    filled_image_1 = fill(pixel_1, seed_point)
    filled_image_2 = fill(pixel_2, seed_point)
    expected_image_1 = [[2]]
    expected_image_2 = [[1]]
    assert(filled_image_1 == expected_image_1)
    assert(filled_image_2 == expected_image_2)

    
# Test for a 1*2 image
def test_small_image():
    small_image = [[0],[1]]
    seed_point_1 = (0,0) # Start at an unfilled pixel
    seed_point_2 = (0,1) # Start at a boundary pixel
    filled_image_1 = fill(small_image, seed_point_1)
    filled_image_2 = fill(small_image, seed_point_2)
    expected_image_1 = [[2],[1]]
    expected_image_2 = [[0],[1]]
    assert(filled_image_1 == expected_image_1)
    assert(filled_image_2 == expected_image_2)


# Test for a 5*6 image with different seed point locations
example_image = [[0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0, 1],
                 [0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0]]

def test_seed_point_in_middle():
    seed_point = (2,4)
    filled_image = iterative_fill(example_image, seed_point)   
    expected_image = [[0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 1, 0],
                      [0, 1, 2, 2, 2, 1],
                      [0, 0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]] 
    assert(filled_image == expected_image)


def test_seed_point_on_bottom():
    seed_point = (3,1)
    filled_image = iterative_fill(example_image, seed_point)   
    expected_image = [[0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 1, 0],
                      [2, 1, 0, 0, 0, 1],
                      [2, 2, 1, 1, 1, 2],
                      [2, 2, 2, 2, 2, 2]]
    assert(filled_image[2] == expected_image[2])


def test_seed_point_on_top():
    seed_point = (0,5)
    filled_image = iterative_fill(example_image, seed_point)   
    expected_image = [[2, 2, 2, 2, 2, 2],
                      [1, 2, 1, 1, 1, 2],
                      [0, 1, 0, 0, 0, 1],
                      [0, 0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]]
    assert(filled_image == expected_image)    
    

# Test for a 15*15 image
load.



# Test for invalid seed points
def test_non_integer_seedpoint():
    seed_point = (2.5,3) 
    filled_image = iterative_fill(example_image, seed_point)
    assert(filled_image == example_image)

def test_seedpoint_with_negative_coordinate():
    seed_point = (-1,3) 
    filled_image = iterative_fill(example_image, seed_point)
    assert(filled_image == example_image)
   
def test_outbound_seedpoint():
    seed_point = (6,3) 
    filled_image = iterative_fill(example_image, seed_point)
    assert(filled_image == example_image)
    
def test_seedpoint_at_boundary():
    seed_point = (2,1) 
    filled_image = iterative_fill(example_image, seed_point)
    assert(filled_image == example_image)

    
test_one_pixel()
test_small_image()
test_seed_point_in_middle()
test_seed_point_on_bottom()
test_seed_point_on_top()
test_non_integer_seedpoint()
test_seedpoint_with_negative_coordinate()
test_outbound_seedpoint()
test_seedpoint_at_boundary()
