def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False


def main():
    # Test cases to validate the solution
    print(in_range(5, 1, 10))  # True: 5 is between 1 and 10
    print(in_range(0, 1, 10))  # False: 0 is not between 1 and 10
    print(in_range(10, 1, 10)) # True: 10 is between 1 and 10, inclusive
    print(in_range(11, 1, 10)) # False: 11 is not between 1 and 10


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
