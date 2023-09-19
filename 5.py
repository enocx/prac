def brute(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


def divide_con(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return divide_con(a*a, n//2)
    else:
        return a * divide_con(a*a, n//2)


a = int(input("Enter the value of a: "))
n = int(input('Enter the value of n: '))

result_of_brute = brute(a, n)
result_of_divide_con = divide_con(a, n)

print(f"Result using bruteforce: {result_of_brute}")
print(f"Result of divide and conquer: {result_of_divide_con}")
