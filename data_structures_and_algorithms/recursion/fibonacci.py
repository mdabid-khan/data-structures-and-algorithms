def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = 10
print(f"First {num} terms of fibonacci series:")

for i in range(num):
    print(fibonacci(i), end=" ")