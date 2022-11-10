def fourth_place(list1: list):
    """fourth_place will return 4th item on list and if list has less, filter out IndexError and return string

    Args:
        list1 (list): list of items 

    Returns:
        4th item: if list has 4 or more items will return 4th if not will return str
    """
    try:
        return list1[3]
    except IndexError:
        print("There is less than 4 items in this list")


def subtracter_lambda(x, y): return x - y

"""lambda func take two integers subtracts y from x and returns answer 
    """


print(subtracter_lambda(10, 6))
