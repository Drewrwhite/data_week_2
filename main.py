people = ["Drew", "Brandyne", "Burke", "Charlie"]
doggos = ["Aengus", "Bear", "Cali"]

def fourth_place(list1: list) -> str:
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
  def __init__(self, US_size: int, color: str, smelly = False) -> None:
    """ Create shoe class that takes size, color and smelly

    Args:
        US_size (int): shoe size US
        color (str): color of shoes
        smelly (bool, optional): are shoes smelly.  Defaults to False.
    """
    self.US_size = US_size
    self.color = color
    self.smelly = smelly
  def euro_size(self) -> None:
    """ takes US_size and converts to Euro size

    Returns:
        String : with Euro sizing
    """
    print(str(self.US_size + 33) + " Euro size")

# two "Shoe" instances to test euro size
vans = Shoe(11, "black", False)
nike = Shoe(10, "green", False)
# print euro size result
vans.euro_size()
nike.euro_size()

def galaxy(galaxy_name: str, *objects_found: str, pluto_is_planet = True, **planets: str) -> None:
  """ galaxy takes arguments and creates paragraph summarizing facts of given info

  Args:
      galaxy_name (str): name of galaxy
      *objects_found (str): lists objects found in galaxy
      pluto_is_planet (bool, optional): Defaults to True. states pluto is planet
      **planets (str): takes value pairs of key as planet and value as color
      
  """
  #print summary of info in arguments
  print(f"Your galaxy is the {galaxy_name}! There are many things contained within the {galaxy_name} including: {objects_found}. Some people dont believe that pluto is a planet and some do. If False you don't, if True, you do! What you think: {pluto_is_planet}. There are more than {len(planets.items())} planets in the {galaxy_name} but the colors of the {len(planets.items())} planets selected are: ")
  for key, value in planets.items():
    print(f"{key} - {value}")
#calling galaxy function with inputs
galaxy("Milky Way Galaxy", "sandworms", "spice", "asteroids", "poison snoopers", "ornihopters", Arrakis = "red and tan", Caladan = "azure and crimson", Poritrin = "tan", Richese = "green an and blue")



