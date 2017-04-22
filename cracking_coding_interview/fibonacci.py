def fibonacci(n):
    # Write your code here.
    fibs = [0, 1]
    for i in range(2, 41):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs[n]



print fibonacci(40)
# fibonacci(6)
