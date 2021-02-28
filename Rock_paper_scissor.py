"""
Plan:
get userinput -> between (1,2,3) 
make random number between(1,2,3) -> computer input
start making comparision to find out who lost,won,ties
"""
import random as r

def user_input():
    print("Welcome to Rock Paper scissor")
    try:
        print("1) Rock\n2) Paper\n3) Scissor")
        number = input(": ")
        assert number in (1,2,3)
    except ValueError: 
        print("Please enter a number !!")
        return user_input()

    else:
        return device_input(number)

def device_input(user:int):
    device = r.randint(1, 3)

    if user == device:
        return "It is a tie"
    
    elif user == 1 and device == 2:
        return "Rock vs Paper\nYou lost :("

    elif user == 2 and device == 3:
        return "Paper vs Scissor\nYou lost :("
    
    elif user == 2 and device == 1:
        return "Paper vs Rock\nYou Won :D"

    elif user == 3 and device == 2:
        return "Scissor vs Paper\nYou Won :D"
    
