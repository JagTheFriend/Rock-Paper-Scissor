"""
Plan:
get userinput -> between (1,2,3) 
make random number between(1,2,3) -> computer input
start making comparision to find out who lost,won,ties
"""
def get_input():
    print("Welcome to Rock Paper scissor")
    try:
        print("1) Rock\n2) Paper\n3) Scissor")
        number = input(": ")
    except ValueError: 
        print("Please enter a number !!")
        return get_input()

    else:
        pass

