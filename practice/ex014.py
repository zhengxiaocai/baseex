# https://www.codewars.com/kata/581f4ac139dc423f04000b99


from itertools import zip_longest


def transpose_two_strings(arr):
    return '\n'.join(f'{i} {j}' for i, j in zip_longest(*arr, fillvalue=' '))


if __name__ == '__main__':
    print(transpose_two_strings(["Hello", "World"]) == "H W\ne o\nl r\nl l\no d")
    print(transpose_two_strings(["joey", "louise"]) == "j l\no o\ne u\ny i\n  s\n  e")
    print(transpose_two_strings(["a", "cat"]) == "a c\n  a\n  t")
    print(transpose_two_strings(["cat", ""]) == "c  \na  \nt  ")
    print(transpose_two_strings(["!a!a!", "?b?b"]) == "! ?\na b\n! ?\na b\n!  ")


