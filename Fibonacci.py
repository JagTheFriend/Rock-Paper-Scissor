"""
Create a fibinacci sequnce,
which takes nth starting number,nth ending number and 
nth number of times repeated.
"""

def Fibonacci(start,end,step):
    for i in range(step):
        sums = start + end
        print(sums,end=" ")
        end = start
        start = sums