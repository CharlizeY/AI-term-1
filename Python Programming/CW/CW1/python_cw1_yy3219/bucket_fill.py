""" Coursework 1: Bucket Fill
"""
import copy
import random

def load_image(filename):
    """ Load image from file made of 0 (unfilled pixels) and 1 (boundary pixels) and 2 (filled pixel)

    Example of content of filename:

0 0 0 0 1 1 0 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 1 0 0 1 0 1 1 0
1 1 0 0 1 0 1 0 1 1
1 0 0 1 0 0 1 0 0 1
1 0 0 1 0 0 1 0 0 1
1 1 0 1 0 0 1 0 1 1
0 1 1 0 1 1 0 1 1 0
0 0 1 1 0 0 1 1 0 0
0 0 0 0 1 1 0 0 0 0

    Args:
        filename (str) : path to file containing the image representation

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel
               2 represents a filled pixel
    """

    image = []
    with open(filename) as imagefile:
        for line in imagefile:
            if line.strip():
                row = list(map(int, line.strip().split()))
                image.append(row)
    return image


def stringify_image(image):
    """ Convert image representation into a human-friendly string representation

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)

    Returns:
        str : a human-friendly string representation of the image
    """
    
    if image is None:
        return ""

    # The variable "mapping" defines how to display each type of pixel.
    mapping = {
        0: " ",
        1: "*",
        2: "0"
    }

    image_str = ""
    if image:
        image_str += "_ " * (len(image[0]) + 2) + "\n"
    for row in image:
        image_str += "| "
        for pixel in row:
            image_str += mapping.get(pixel, "?") + " "
        image_str += "|"
        image_str += "\n"
    if image:
        image_str += "‾ " * (len(image[0]) + 2) + "\n"

    return image_str


def show_image(image):
    """ Show image in terminal

    Args:
        image (list) : list of lists of 0 (unfilled pixel), 1 (boundary pixel) and 2 (filled pixel)
    """
    print(stringify_image(image))


## My function
def is_unfilled(image, row, col):
    '''
    Check whether a pixel is unfilled, i.e. has label 0. 
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
    """ Fill the image from seed point to boundary

    the image should remain unchanged if:
    - the seed_point has a non-integer coordinate
    - the seed_point has a negative coordinate
    - the seed_point is outside of the image
    - the seed_point is on a boundary pixel
    
    Args:
        image (list) : a 2D nested list representation of an image, where
                       0 represents an unfilled pixel, and
                       1 represents a boundary pixel
        seed_point (tuple) : a 2-element tuple representing the (row, col) 
                       coordinates of the seed point to start filling

    Returns:
        list : a 2D representation of the filled image, where
               0 represents an unfilled pixel,
               1 represents a boundary pixel, and
               2 represents a filled pixel
    """
    row = seed_point[0]
    col = seed_point[1]
    filled_image = copy.deepcopy(image) # To ensure that image remains unchanged in test cases
    
    if (isinstance(row, int) and isinstance(col, int)) == False:
        # print("The seed point has a non-integer coordinate.")
        return filled_image
        
    if row < 0 or col < 0:
        # print("The seed point has a negative coordinate.") 
        return filled_image
    
    if row > len(filled_image) - 1 or col > len(filled_image[0]) - 1:
        # print("The seed point is outside the image.") 
        return filled_image
    
    if filled_image[row][col] == 1:
        # print("The seed point is on a boundary pixel.") 
        return filled_image

    p = []  # Initiate an empty list of points
    filled_image[row][col] = 2  # Fill the seed point 
    p.append((row, col))  # Add the seed point to the list

    while len(p) > 0:
        (cur_row, cur_col) = p[0]
        del p[0] # To ensure that new neighbouring points are explored

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
    filled_image = fill(example_image, seed_point)   
    expected_image = [[0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 1, 0],
                      [0, 1, 2, 2, 2, 1],
                      [0, 0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]] 
    assert(filled_image == expected_image)


def test_seed_point_on_bottom():
    seed_point = (3,1)
    filled_image = fill(example_image, seed_point)   
    expected_image = [[0, 0, 0, 0, 0, 0],
                      [1, 0, 1, 1, 1, 0],
                      [2, 1, 0, 0, 0, 1],
                      [2, 2, 1, 1, 1, 2],
                      [2, 2, 2, 2, 2, 2]]
    assert(filled_image[2] == expected_image[2])


def test_seed_point_on_top():
    seed_point = (0,5)
    filled_image = fill(example_image, seed_point)   
    expected_image = [[2, 2, 2, 2, 2, 2],
                      [1, 2, 1, 1, 1, 2],
                      [0, 1, 0, 0, 0, 1],
                      [0, 0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]]
    assert(filled_image == expected_image)    
    

# Test for a 15*15 image
def test_median_image():
    median_image = load_image("data/snake.txt")
    seed_point = (3,6)
    filled_image = fill(median_image, seed_point)
    expected_image = [[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0],
                      [0, 0, 1, 2, 1, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0],
                      [0, 0, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 0, 0, 0],
                      [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0],
                      [0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                      [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                      [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0]]
    assert(filled_image == expected_image)


# Test for cases of invalid seed points
# On the 5*6 image as an example
def test_non_integer_seedpoint():
    seed_point = (2.5,3) 
    filled_image = fill(example_image, seed_point) 
    assert(filled_image == example_image)

def test_seedpoint_with_negative_coordinate():
    seed_point = (-1,3) 
    filled_image = fill(example_image, seed_point)
    assert(filled_image == example_image)
   
def test_outbound_seedpoint():
    seed_point = (6,3) 
    filled_image = fill(example_image, seed_point)
    assert(filled_image == example_image)
    
def test_seedpoint_at_boundary():
    seed_point = (2,1) 
    filled_image = fill(example_image, seed_point)
    assert(filled_image == example_image)


# Running the tests   
test_one_pixel()
test_small_image()
test_median_image()
test_seed_point_in_middle()
test_seed_point_on_bottom()
test_seed_point_on_top()
test_non_integer_seedpoint()
test_seedpoint_with_negative_coordinate()
test_outbound_seedpoint()
test_seedpoint_at_boundary()


def example_fill():
    image = load_image("data/bar.txt")

    print("Before filling:")
    show_image(image)

    image = fill(image=image, seed_point=(7, 3))

    print("-" * 25)
    print("After filling:")
    show_image(image)


if __name__ == '__main__':
    example_fill()
