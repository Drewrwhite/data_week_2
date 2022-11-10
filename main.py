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

#lambda function that takes teo numbers and subtracts number 2 from number 1
subtracter_lambda = lambda x, y: x - y
print(subtracter_lambda(10,6))

class Shoe: # create shoe class
  def __init__(self, US_size: int, color: str, smelly = False: bool):
    """ Create shoe class that takes size, color and smelly

    Args:
        US_size (int): shoe size US
        color (str): color of shoes
        smelly (bool, optional): are shoes smelly.  Defaults to False.
    """
    self.US_size = US_size
    self.color = color
    self.smelly = smelly
  def euro_size(self):
    """ takes US_size and converts to Euro size

    Returns:
        String : with Euro sizing
    """
    print ()str(self.US_size + 33) + " Euro size"

# two "Shoe" instances to test euro size
vans = Shoe(11, "black", False)
nike = Shoe(10, "green", False)
# print euro size result
vans.euro_size()
nike.euro_size()




