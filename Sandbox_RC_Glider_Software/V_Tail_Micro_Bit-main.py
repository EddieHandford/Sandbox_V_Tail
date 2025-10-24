#To Do List
#Take ELRS RC input 
#Mix the Vtail outputs pitch and yaw axis and 
#include option to reverse the servo
#Test system can be manually flown
#Introduce a compass hold mode - ideally toggleable with an RC channel

# Imports go at the top
from microbit import *


#Data_Dictionary
Data_Compass = 0.0



# Code in a 'while True:' loop repeats forever
while True:
    
    Data_Compass = compass.heading()
    
    display.scroll(Data_Compass)
    
    print(Data_Compass)