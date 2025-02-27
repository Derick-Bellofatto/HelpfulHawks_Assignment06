# File Name: GandurpnClass.py
# Student Name: Pransu Justin Ganduri
# Email: gandurpn@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 2/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: In this assignment, we are collaborating with peers to develop a VS project modeling a real-world system.
# Brief Description of what this module does: This module defines the GandurpnClass, which manages crop harvesting, including readiness checks and yield tracking.
# Citations: N/A
# Anything else that's relevant: N/A

class my_class(object):
    pass

class GandurpnClass:
    """
    A class to manage the harvesting of crops in the garden.
    """
    def __init__(self, crop_type="Tomato", is_ready=False, yield_amount=0):
        """
        Initialize the GandurpnClass.
        
        @param crop_type str: The type of crop being harvested
        @param is_ready bool: Whether the crop is ready for harvesting
        @param yield_amount int: The number of crops that can be harvested
        """
        self._crop_type = crop_type
        self._is_ready = is_ready
        self._yield_amount = yield_amount

    def __str__(self):
        """
        Return a readable string representation of the harvest.
        """
        return f"GandurpnClass ({self._crop_type} - Ready: {self._is_ready}, Yield: {self._yield_amount})"
    
    def __repr__(self):
        """
        Return a developer-friendly string representation of the harvest.
        """
        return f"GandurpnClass('{self._crop_type}', {self._is_ready}, {self._yield_amount})"

    @property
    def is_ready(self):
        """
        Getter for the harvest readiness.
        """
        return self._is_ready

    @is_ready.setter
    def is_ready(self, value):
        """
        Setter for the harvest readiness.
        """
        self._is_ready = value

    @property
    def yield_amount(self):
        """
        Getter for the yield amount.
        """
        return self._yield_amount

    @yield_amount.setter
    def yield_amount(self, value):
        """
        Setter for the yield amount. Ensures non-negative values.
        """
        if value >= 0:
            self._yield_amount = value
        else:
            print("Error: Yield amount cannot be negative.")

    def check_harvest(self):
        """
        Check if the crops are ready for harvesting.
        """
        if self._is_ready:
            print(f"The {self._crop_type} is ready for harvest! Yield: {self._yield_amount}")
        else:
            print(f"The {self._crop_type} is not ready yet.")

    def harvest_crops(self):
        """
        Harvest the crops if they are ready.
        """
        if self._is_ready:
            print(f"Harvesting {self._yield_amount} {self._crop_type}(s)...")
            self._is_ready = False  # Reset readiness after harvesting
            self._yield_amount = 0  # Reset yield after harvest
        else:
            print(f"The {self._crop_type} is not ready to be harvested yet.")

# Testing the class
if __name__ == "__main__":
    test_harvest = GandurpnClass("Carrot", True, 15)
    print(repr(test_harvest))
    test_harvest.check_harvest()
    test_harvest.harvest_crops()
    test_harvest.check_harvest()




