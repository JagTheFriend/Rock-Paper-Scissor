"""
Create a fibinacci sequnce,
which takes nth starting number,nth ending number and 
nth number of times repeated.
"""

def Fibonacci(start,end,step):
    print(start, end,end=" ")
    for i in range(step-2):
        sums = start + end
        print(sums,end=" ")
        end = start
        start = sums

def get_number():
    try:
        start = int(input("Please enter the start value: "))
        end = int(input("Please enter the end value: "))
        step = int(input("Please enter the number of numbers: "))

    except ValueError:
        print("Please enter a whole number !!")
        return get_number()
    
    else: 
        return Fibonacci(start, end, step)

get_number()