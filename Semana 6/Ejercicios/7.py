def is_prime(num):
    if num <= 1:
        return False

    sqrt_floor = int(num**0.5)
    for i in range(2, sqrt_floor + 1):
        if num % i == 0:
            return False

    return True


def get_primes(numbers):
    prime_numbers = []

    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers


def main():
    numbers = [1, 4, 6, 7, 13, 9, 67]
    primes = get_primes(numbers)
    print(primes)


main()
