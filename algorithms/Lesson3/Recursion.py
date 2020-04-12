"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib(position):
    fibo = []
    if position <= 0:
        fibo.append(0)
        return fibo
    else:
        fibo = get_fib(position - 1)
        if len(fibo) <= 1:
            fibo.append(1)
        else:
            fibo.append(fibo[position - 2] + fibo[position - 1])
    return fibo


# Test cases
print(get_fib(3).pop())
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
