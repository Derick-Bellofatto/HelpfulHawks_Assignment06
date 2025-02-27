# File Name : Nairapclass.py
# Student Name: Annapoorna Nair
# email:  nairap@mail.uc.ed
# Assignment Number: Assignment 06
# Due Date:   Feb 27,2025
# Course #/Section:   IS 4010 Section 1
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We are practcing making classes

# Brief Description of what this module does. This makes a class that has methods related to plant status, pests, and weeds
# Citations: I based a lot of this code on the Inclass Assignment we did last Thursday

class PlantCare:
    """
    Model a plant needing some tough love. Includes figuring out what plant this even is, its current state,
    weeds, and killing scale bugs. We will add a property to make a plant change color to symbolize its dying.
    """

    def __init__(self, plant_type, color='Green', weeds=None, pests=None):
        """
        Constructor to initialize the plant with type, color, weeds, and pests.
        (@param plant_type String: The type of plant)
        (@param color String: The color of the plant, defaults to 'Green')
        (@param weeds List: Optional list of weeds, defaults to None)
        (@param pests List: Optional list of pests, defaults to None)
        """
        self.set_type(plant_type)
        self.set_color(color)
        self.set_weeds(weeds if weeds else ())
        self.set_pests(pests if pests else ())

    def get_type(self):
        """
        (@return String: The type of plant)
        """
        return self.__type

    def set_type(self, plant_type):
        """
        Assign a value to the type of plant the current object is.
        (@param plant_type String: The plant species to be assigned)
        """
        if not plant_type or len(plant_type.strip()) == 0:
            raise Exception("PlantCare Class: Plant species must be provided.")
        self.__type = plant_type

    def get_color(self):
        """
        (@return String: The color of the plant)
        """
        return self.__color

    def set_color(self, color):
        """
        Assign a value to the color of the plant.
        (@param color String: The plant color to be assigned)
        """
        if not color or len(color.strip()) == 0:
            raise Exception("PlantCare Class: Color cannot be an empty string.")
        self.__color = color

    def get_weeds(self):
        """
        (@return weeds: The list of weeds affecting the plant)
        """
        return self.__weeds

    def set_weeds(self, weeds):
        """
        Assign a value to the list of weeds affecting the plant.
        (@param weeds List: The list of weeds to be assigned)
        """
        self.__weeds = weeds

    def get_pests(self):
        """
        (@return pests: The pests affecting the plant)
        """
        return self.__pests

    def set_pests(self, pests):
        """
        Assign a value to the list of pests affecting the plant.
        """
        self.__pests = pests

    def print_type(self):
        """
        Print the plant species of the current object.
        """
        print(f"Plant Species: {self.__type}")

    def print_color(self):
        """
        Print the plant color of the current object.
        """
        print(f"Plant Color: {self.__color}")

    def print_weeds(self):
        """
        Print the weeds affecting the plant.
        """
        print(f"Weeds: {', '.join(self.__weeds) if self.__weeds else 'None'}")

    def print_pests(self):
        """
        Print the pests affecting the plant.
        """
        print(f"Pests: {', '.join(self.__pests) if self.__pests else 'None'}")

    def __str__(self):
        """
        (@return String: A human-readable basic representation of the current object)
        """
        return f"Plant Type: {self.__type}, Color: {self.__color}, Weeds: {', '.join(self.__weeds) if self.__weeds else 'None'}, Pests: {', '.join(self.__pests) if self.__pests else 'None'}"

    def __repr__(self):
        """
        (@return String: A string containing code that can be executed to create a copy of the current object)
        """
        return f"PlantCare('{self.__type}', '{self.__color}', {self.__weeds}, {self.__pests})"

    """
    This is Test Case stuff:
    
    from Nairap.Nairapclass import *

    if __name__ == "__main__":
    plants = PlantCare ("Forget-me-not","brown") 
    print(type(plants))
    color = PlantCare ("brown")
    pests = PlantCare ("scalebugs")
    weeds = PlantCare ("Dandelions")

    print("What species of plant do we got here? It's a", plants.get_type()) 

    print("This poor thing used to be green, now it's", color.get_type()) 

    print ("The", plants.get_type(),"has",pests.get_type(),"and", weeds.get_type())
    print("Seems like we have a lot of work to make this place healthy again.")

    """












