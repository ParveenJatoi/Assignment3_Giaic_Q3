import random

# Set the likelihood of stopping early (between 0.0 and 1.0)
DONE_LIKELIHOOD = 0.3

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Ends the function execution and returns to main
        print(curr_num)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# This provided line is required at the end of the Python file to call main()
if __name__ == '__main__':
    main()
