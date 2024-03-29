#!/usr/bin/python

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def main():
    # Small optimization here by using dictionary-storage to remember previous
    # values instead of recomputing the entire chain
    d = {1:1, 2:2}
    total = 0 # Total summation
    current = d[2] # Current value...this is fib(position)
    position = 3 # The index of the number in the sequence
    threshold = 4000000 # do not exceed 4 million
    
    while current < threshold:
        d = fib(d,position)
        current = d[position]
        position += 1
        
    for key in d.keys():
        if d[key] < threshold:
            if d[key] % 2 == 0:
                total += d[key]
    
    print "Sum of even-valued terms of Fibonacci sequence whose values do not exceed 4M: %d" % total
    
    
def fib(d, n):
    d[n] = d[n-2] + d[n-1]
    return d
    
if __name__ == "__main__":
    main()