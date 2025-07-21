# --TASK-1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))



# --TASK-2
def digit_sum(k):
    return sum(map(int, str(k)))

print(digit_sum(24))
print(digit_sum(502))  




# --TASK-3
def powers_of_two(N):
    result = []
    i = 1
    while (2 ** i) <= N:
        result.append(2 ** i)
        i += 1
    print(*result)

powers_of_two(10)
