# Day 14 : Write a program to print the first n numbers of a Fibonacci sequence

def fibonacci_sequence(n):

# initialize the list fib_seq, with the first 2 fibonacci numbers 0 and 1
    fib_seq = [0,1]

# generate 'for' loop to generate the fibonacci numbers.
# [i - 2 ] : tells you the list index location 
    for i in range(2, n):
        next_num = fib_seq[i - 1] + fib_seq[i-2]
        fib_seq.append(next_num)
    return fib_seq[:n]

n = int(input("Enter the value of n: "))

result = fibonacci_sequence(n)

print(f"The first {n} numbers of the Fibonacci sequence are: {result}")
