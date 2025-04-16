def get_user_info():
    # Ask for user details and store them in variables
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")
    
    # Return all the gathered data as a tuple
    return first_name, last_name, email_address

########## No need to edit code past this point :) ##########

def main():
    # Call get_user_info() and store the returned tuple in user_data
    user_data = get_user_info()
    
    # Print the received user data
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
