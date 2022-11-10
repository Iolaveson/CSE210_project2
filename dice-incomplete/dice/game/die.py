import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.die = []
        self.value = None
        self.points = None

# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        for i in range(5):
            self.value = random.randint(1, 6)
            self.die.append(self.value)

        self.points = (self.die.count(5)) * 50 + (self.die.count(1)) * 100


        #Abstraction is defined as the process of turning a complex thing or idea into a simple thing or idea.  We use abstraction every day because it helps us break things down into understandable pieces. For example, if we use a built-in function to count the sum of a list we do not have to have as much knowledge as we would need to write a loop to accomplish the same result. That is where the main benefit of abstraction is. With abstraction we only need a surface level understand to utilize something more complex.