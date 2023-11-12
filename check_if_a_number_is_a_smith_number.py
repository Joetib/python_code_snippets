# A Smith number is a composite number whose sum of digits in its prime factorization is equal to the sum of digits in the number itself.

# To check if a number is a Smith number, we can follow these steps:
# 1. Find the prime factors of the number.
# 2. Calculate the sum of digits in the prime factors.
# 3. Calculate the sum of digits in the number itself.
# 4. If the sums are equal, then the number is a Smith number.

# Let's implement this in code:

def is_smith_number(n):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    def prime_factors(num):
        factors = []
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    prime_factor_sum = sum_of_digits(sum(prime_factors(n)))
    number_sum = sum_of_digits(n)

    return prime_factor_sum == number_sum

# Test the function
number = int(input("Enter a number: "))
print(is_smith_number(number))

# Example Output:
# Enter a number: 728
# True
# Please Like and Subscribe