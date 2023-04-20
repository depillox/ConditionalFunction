#Name: Zavier DePillo
#Email: depillzj@mail.uc.edu
#Assignment Title: Assignment 03
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: This project demonstrates that I can write a conditional function and test it with the provided code
#Citations:
#Anything else that's relevant:

from functionsPackage.functions import *


count_passed = 0
count_failed = 0
if (is_divisible(15) == True):
    print("Test #1 passed")
    count_passed = count_passed + 1
else:
    print("Test #1 FAILED")
    count_failed = count_failed + 1
if (is_divisible(1) == False):
    print("Test #2 passed")
    count_passed = count_passed + 1
else:
    print("Test #2 FAILED")
    count_failed = count_failed + 1
if (is_divisible(5) == False):
    print("Test #3 passed")
    count_passed = count_passed + 1
else:
    print("Test #3 FAILED")
    count_failed = count_failed + 1
if (is_divisible(0) == True):
    print("Test #4 passed")
    count_passed = count_passed + 1
else:
    print("Test #4 FAILED")
    count_failed = count_failed + 1
if (is_divisible(390) == True):  #New test added
    print("Test #5 passed")
    count_passed = count_passed + 1
else:
    print("Test #5 FAILED")
    count_failed = count_failed + 1
print(str(count_passed) + " tests passed and " + str(count_failed) + " tests failed")