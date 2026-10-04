def find_fibonacci(num, cache):
    if num == 0:
        return 0

    if num == 1:
        return 1

    if num in cache:
        return cache[num]

    cache[num] = find_fibonacci(num - 1, cache) + find_fibonacci(num - 2, cache)
    return cache[num]


number = int(input("Enter the number: "))
cache = {}

print("Fibonacci result:", find_fibonacci(number, cache))
print("Stored values:", cache)