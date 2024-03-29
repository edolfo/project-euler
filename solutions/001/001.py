#!/usr/bin/python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    total = 0
    for i in range(1, 1000): # exclude 1000, as the problem wants nats below 1000
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    print "Sum of natural numbers divisible by 3 or 5 under 1000 is %d" % total
    
if __name__ == "__main__":
    main()