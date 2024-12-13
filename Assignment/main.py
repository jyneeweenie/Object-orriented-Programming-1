class Robot:
    # class attribute
    species = "robot"
    # instance attribute
    def __init__(self, name):
        self.name = name
# instantiate the Parrot class
tom = Robot("Tom")
jerry = Robot("Jerry")
# access the class attributes
print("Tom is a {}".format(tom.species))
print("Jerry is alo a {}".format(jerry.species))
