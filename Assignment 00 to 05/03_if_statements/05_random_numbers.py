import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    """
    Prints 10 random numbers between 1 and 100.
    Each run will produce different random numbers.
    """
    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number)

if __name__ == '__main__':
    main()
