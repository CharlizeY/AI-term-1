from q1 import odd_even_swap


def test1():
    word = "abcdefghi"
    swapped = odd_even_swap(word)
    expected = "badcfehgi"
    assert swapped == expected


def test2():
    word = "Python Programming"
    swapped = odd_even_swap(word)
    expected = "yPhtnoP orrgmaimgn"
    print(swapped)
    assert swapped == expected


if __name__ == "__main__":
    test1()
    test2()

