# We can use a helper function to check if a number is prime or not.
# Then, we can iterate through the given range and check if each number is prime.
# If a number is prime, we update the largest prime number found so far.
# Finally, we return the largest prime number.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime(start, end):
    largest_prime = None
    for num in range(start, end + 1):
        if is_prime(num):
            largest_prime = num
    return largest_prime

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

largest_prime = find_largest_prime(start, end)
print(largest_prime)

# Example usage:
# Enter the starting number: 1
# Enter the ending number: 20
# Output: 19
# Please Like and Subscribe