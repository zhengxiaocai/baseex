# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

"""
The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    def c(n):
        if n < 0:
            n = 0
        if n > 255:
            n = 255
        return n

    return '{:02x}{:02x}{:02x}'.format(c(r), c(g), c(b)).upper()


def rgb_best(r, g, b):
    round = lambda x: min(255, max(0, x))
    return ('{:02X}' * 3).format(round(r), round(g), round(b))


if __name__ == '__main__':
    print(rgb(0, 0, 0) == "000000")
    print(rgb(1, 2, 3) == "010203")
    print(rgb(255, 255, 255) == "FFFFFF")
    print(rgb(254, 253, 252) == "FEFDFC")
    print(rgb(-20, 275, 125) == "00FF7D")

    print(rgb_best(0, 0, 0) == "000000")
    print(rgb_best(1, 2, 3) == "010203")
    print(rgb_best(255, 255, 255) == "FFFFFF")
    print(rgb_best(254, 253, 252) == "FEFDFC")
    print(rgb_best(-20, 275, 125) == "00FF7D")

    """
        知识点：
        1、简单逻辑用lambda
        2、{:02X}
    """
