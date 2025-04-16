MINIMUM_HEIGHT: int = 50  # arbitrary units :)

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    while True:
        try:
            height_str = input("How tall are you? ")
            if not height_str:  # If user just presses Enter without typing anything
                break
            height = float(height_str)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for height.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    # Uncomment the line below to run the extension version
    # tall_enough_extension()
    main()
