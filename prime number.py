def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
prime_check = is_prime(9)
print(f"Is 9 prime? {prime_check}")