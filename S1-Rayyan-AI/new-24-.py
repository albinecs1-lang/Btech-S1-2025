#finding power,factorial,squre root of a number 

#importing requerd module
import math as mt

#power
number = 10
powering = int(mt.pow(number , number))

#factorial
factorial = mt.factorial(number)

#squre root
squre_root = int(mt.sqrt(number))

print(f'the power at {number} is {powering} the factorial is {factorial} the squre root is {squre_root}')
