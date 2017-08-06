"""Script to find prime numbers.

This is a first attempt (and written from a non-mathematics background), so there may be more efficient ways to do this.
"""

def divides_fully_against_denominators(target, denominators):
    """Determine of a target integer can be divided by any number amongst a list of denominators, with a remainder of zero.

    Args:
        target (int): A number to test if it is prime against the denominators.
        denominators (list of int): A list of numbers to act as denominators for the target number.

    Returns:
        bool: False if the target number can be fully divided against at least one number in denominators. True if it cannot.
    """
    denominators.sort()
    for num in denominators:
        if target % num == 0:
            return False
    return True


# Load all existing numbers from the file into a list
with open('primes.txt', 'r') as file:
    current_primes = [int(x) for x in file.readlines()]

# Get the largest number
current_largest_prime = max(current_primes)

# Set the current number to test
current_int = current_largest_prime + 1


while True:
    # Test if current_int is a prime
    if divides_fully_against_denominators(current_int, current_primes):
        print('{0} is a prime number'.format(current_int))
        with open('primes.txt', 'a') as file:
            file.write(str(current_int) + '\n')
            current_primes.append(current_int)
            current_largest_prime = current_int
    current_int += 1
