from string import ascii_uppercase 
import random


seed = "Totally random."
random.seed(seed)


class Robot:
    __used_names = set()
    def __generate_name(self):
        while True:
            name = f"""{random.choice(ascii_uppercase)}{random.choice(ascii_uppercase)}{random.randint(0, 999):03d}"""
            if name not in self.__used_names:
                self.__used_names.add(name)
                return name
        
    
    def __init__(self):
        self.name = self.__generate_name()

    def reset(self):
        old_name = self.name


        while True:
            new_name = self.__generate_name()
            if new_name != old_name:
                
                self.__used_names.remove(old_name)
                self.name = new_name
                break


test = Robot()
test2 = Robot()

print(test.name)
test.reset()
print(test.name)



# import unittest
# import random

# class RobotNameTest(unittest.TestCase):
#     # assertRegex() alias to address DeprecationWarning
#     # assertRegexpMatches got renamed in version 3.2
#     if not hasattr(unittest.TestCase, "assertRegex"):
#         assertRegex = unittest.TestCase.assertRegexpMatches
#     name_re = r'^[A-Z]{2}\d{3}$'
#     def test_has_name(self):
#         self.assertRegex(Robot().name, self.name_re)
#     def test_name_sticks(self):
#         robot = Robot()
#         robot.name
#         self.assertEqual(robot.name, robot.name)
#     def test_different_robots_have_different_names(self):
#         self.assertNotEqual(
#             Robot().name,
#             Robot().name
#         )
#     def test_reset_name(self):
#         # Set a seed
#         seed = "Totally random."
#         # Initialize RNG using the seed
#         random.seed(seed)
#         # Call the generator
#         robot = Robot()
#         name = robot.name
#         # Reinitialize RNG using seed
#         random.seed(seed)
#         # Call the generator again
#         robot.reset()
#         name2 = robot.name
#         self.assertNotEqual(name, name2)
#         self.assertRegex(name2, self.name_re)
# if __name__ == '__main__':
#     unittest.main()