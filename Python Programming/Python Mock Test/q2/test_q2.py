from q2 import closest_pair


def test1():
    coord_list = [(1, 2), (3, 5), (5, 4), (2, 1), (5, 2)]
    closest = closest_pair(coord_list)
    expected = {(1, 2), (2, 1)}
    print(closest)
    assert closest == expected


def test2():   
    coord_list = [(1, 1, 1), (2, 3, 1), (3, 3, 2), (1, 3, 3), (4, 1, 1), (3, 4, 4)]
    closest = closest_pair(coord_list)
    expected = {(2, 3, 1), (3, 3, 2)}
    print(closest)
    assert closest == expected


if __name__ == "__main__":
    test1()
    test2()

