# File Name : main.py
# Student Name: Derick Bellofatto
# email:  Bellofdk@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   Feb 27,2025
# Course #/Section:   IS 4010 Section 1
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Practicing the use of git for collaboration in teams

# Brief Description of what this module does. This module calls, then tests each class made. It is also the main gateway

from Gandurpn.GandurpnClass import *
from Painjavv.plants import *
from Nairap.Nairapclass import *

if __name__ == "__main__":

    print("Testing Gandupn file\n")

    test_harvest = GandurpnClass("Carrot", True, 15)
    print(repr(test_harvest))
    test_harvest.check_harvest()
    test_harvest.harvest_crops()
    test_harvest.check_harvest()
    print(test_harvest.__str__)

    
    print("\nTesting Painjavv file\n")


    test_plant = Plant("Melon", "Fruit", False)
    test_plant.water()
    test_plant.grow()
    print("Double checking plant is mature: ")
    test_plant.is_mature
    print(test_plant.is_mature)

    print("\nTesting Nairap file\n")

    plants = PlantCare ("Forget-me-not","brown") 
    print(type(plants))
    color = PlantCare ("brown")
    pests = PlantCare ("scalebugs")
    weeds = PlantCare ("Dandelions")

    print("What species of plant do we got here? It's a", plants.get_type()) 

    print("This poor thing used to be green, now it's", color.get_type()) 

    print ("The", plants.get_type(),"has",pests.get_type(),"and", weeds.get_type())
    print("Seems like we have a lot of work to make this place healthy again.")