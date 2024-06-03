# create a function to calculate the first couple of fibonacci numbers


def fibonacci_calc(n, memory={}):
    if n in memory:
        return memory[n]
    if n <= 0:
        return 1

    memory[n] = fibonacci_calc(n-1, memory) + fibonacci_calc(n-2, memory)

    return memory[n]


def fibonacci_sequencing(start, end):
    fib_seq = []

    for i in range(start - 1, end + 1):
        fib_seq.append(fibonacci_calc(i))

    return fib_seq


fib_num = fibonacci_sequencing(0, 10)
print(fib_num)
