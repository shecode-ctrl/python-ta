import sys
import os


def prime(s):
    # your code goes here
# Program to check if a number is prime or not

    programState = False

# prime numbers are greater than 1
    if s > 1:
    # check for factors
        for i in range(2, s):
            if (s % i) == 0:
            # if factor is found, set programState to True
                programState = True
            # break out of loop
            break

# check if flag is True
    if programState:
        print(s, "is not a prime number")
    else:
        print(s, "is a prime number")


def solution(s):
    return prime(s)


if _name_ == "_main_":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))