# Affirmation the user needs to type
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # First prompt
    print("Please type the following affirmation: " + AFFIRMATION)

    # Get user input
    user_input = input()

    # Loop until the correct affirmation is typed
    while user_input != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()

    # Success message
    print("That's right! :)")

# Run the program
if __name__ == '__main__':
    main()
