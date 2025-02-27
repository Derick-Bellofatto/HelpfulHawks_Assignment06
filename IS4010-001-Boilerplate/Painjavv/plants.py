# File Name : plants.py
# Student Name: Vishwaja Painjane
# email: painjavv@mail.uc.edu
# Assignment Number: Assignment06
# Due Date: 27th February, 2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment was a group project in which we modeled something from the real world: a garden.
# Brief Description of what this module does: This module shows how we can create real life things with classes and modules.
# Citations:  Automate the boring stuff with python (https://automatetheboringstuff.com/2e/chapter3/), GeeksforGeeks(https://www.geeksforgeeks.org/python-basics/#python-functions), ChtGPT(https://openai.com/index/chatgpt/)
# Anything else that's relevant: N/A

# plants.py

class Plant:
    """
    A class to represent a plant in a garden.
    Attributes:
    name : str - The name of the plant (e.g., 'Rose', 'Carrot').
    plant_type : str - The type of the plant (e.g., 'flower' or 'vegetable').
    is_mature : bool - A flag indicating if the plant is mature or not (default is False).
    """

    def __init__(self, name, plant_type, is_mature=False):
        """
        Set a new plant with the given name, type, and maturity status.
        @param name: string - The name of the plant.
        @param plant_type: string - The type of the plant ('flower' or 'vegetable').
        @param is_mature: bool, optional - The maturity status of the plant (default is False).
        @result - A new Plant object is created with the provided name, type, and maturity status.
        """
        self.name = name
        self.plant_type = plant_type  # 'flower' or 'vegetable'
        self.is_mature = is_mature

    @property
    def is_mature(self):
        """
        Get the current maturity status of the plant.
        @result: bool - Returns whether the plant is mature (True) or not (False).
        """
        return self._is_mature

    @is_mature.setter
    def is_mature(self, value):
        """
        Set a new maturity status for the plant.
        @param value: bool The new maturity status to set for the plant (True or False).
        @result: The plant's maturity status is updated to the new value.
        """
        self._is_mature = value

    def water(self):
        """
        Water the plant.
        @result - Prints a message indicating that the plant is being watered.
        """
        print(f"Watering plant: {self.name}")

    def grow(self):
        """
        Set the plant to mature if it is not already.
        @result - If the plant is not mature, it becomes mature and prints a message indicating the plant has grown.
        """
        if not self.is_mature:
            self.is_mature = True
            print(f"{self.name} has grown and is now mature!")

    def __str__(self):
        """
        Get a user-friendly string representation of the plant.
        @result: string - Returns a string with the plant's name, type, and maturity status.
        """
        return f"Plant: {self.name}, Type: {self.plant_type}, Mature: {self.is_mature}"

    def __repr__(self):
        """
        Get a detailed string representation of the plant for debugging.
        @result: string - Returns a detailed string representation of the plant with its name, type, and maturity status.
        """
        return f"Plant(name='{self.name}', type='{self.plant_type}', mature={self.is_mature})"


