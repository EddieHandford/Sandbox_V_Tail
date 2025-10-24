#To Do List
#Take ELRS RC input 
#Mix the Vtail outputs pitch and yaw axis and 
#include option to reverse the servo
#Test system can be manually flown
#Introduce a compass hold mode - ideally toggleable with an RC channel

# Imports go at the top
from microbit import *


#Data_Dictionary

Data_Compass = 0.0  #Appears to return as an INT

RC_Input_Channel_1 = 1500
RC_Input_Channel_2 = 1500
RC_Input_Channel_3 = 1500
RC_Input_Channel_4 = 1500
RC_Input_Channel_5 = 1500
RC_Input_Channel_6 = 1500
RC_Input_Channel_7 = 1500
RC_Input_Channel_8 = 1500

V_Tail_Port_Servo_Output = 1500
V_Tail_Starboard_Servo_Output = 1500


# Code in a 'while True:' loop repeats forever
while True:
    
    Data_Compass = compass.heading()
    
    display.scroll(Data_Compass)
    
    print(Data_Compass)