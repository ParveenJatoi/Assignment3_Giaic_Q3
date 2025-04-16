def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b.
    """
    return (a + b) / 2


def main():
    # Example averages
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)

    # Average of two averages
    final = average(avg_1, avg_2)

    # Output results
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
