"""EX04 - list Utility Functions"""

__author__ = "730469489"


def all(a: list[int], b: int) -> bool:
    """returns bool on whether or not all list elements equal the int"""

    if a == []:
        """if a is an empty list, return false"""
        return False
        """initalization count variable"""
    count = 0

    for i in a:
        """looping through every list element"""

        if i == b:
            """comparing it to b and incrementing count"""
            count += 1
    if count == len(a):
        """if the count equals the total elements in a, then all elements in a equal b"""
        return True
    else:
        return False


def max(a: list[int]) -> int:
    """gives the largest integer in a"""
    if len(a) == 0:
        """if the length of a is equal to 0, the list is empty"""
        raise ValueError("max() arg is an empty List")

    temp = a[0]
    """sets temp var to first element in list to prepare for comparison"""
    for i in a:
        """for loop to compare if element is greater than temp"""
        if i > temp:

            temp = i
            """sets temp to new highest int"""
    return temp


def is_equal(a: list[int], b: list[int]) -> bool:
    """checks if the two lists are equal to each other"""
    if len(a) != len(b):
        """returns false if the number of elements dont match"""
        return False
    for i in range(len(a)):
        """for loop that checks of the index of both list dont equal to each other"""
        if a[i] != b[i]:
            return False
    return True


def extend(a: list[int], b: list[int]) -> None:
    """appends each element of b to a"""
    for i in b:
        """uses append method to add i elements to the a list"""
        a.append(i)
    return None
