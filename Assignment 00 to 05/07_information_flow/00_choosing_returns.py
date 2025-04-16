ADULT_AGE = 18  # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

########## No need to edit code beyond this point :) ##########

def main():
    age = int(input("How old is this person?: "))  # Corrected to cast input to int
    print(is_adult(age))

if __name__ == "__main__":
    main()
