def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_factorization(n):
    for i in range(2, n+1):
        if is_prime(i):
            x = i
            while n % x == 0:
                print(i, end=' ')
                x = x * i


if __name__ == '__main__':
    n = int(input('Enter a number: '))
    prime_factorization(n)