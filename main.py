def menu():
    while True:
        print("\nChoose an operation.......")
        print("1. Make a list")
        print("2. Make a tuple")
        print("3. Make a set")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Create a list
            user_input = input("Enter elements for the list (comma separated): ")
            user_list = user_input.split(',')  # Split the input string by commas
            print("Your list:", user_list)

        elif choice == '2':
            # Create a tuple
            user_input = input("Enter elements for the tuple (comma separated): ")
            user_tuple = tuple(user_input.split(','))  # Convert to tuple
            print("Your tuple:", user_tuple)

        elif choice == '3':
            # Create a set
            user_input = input("Enter elements for the set (comma separated): ")
            user_set = set(user_input.split(','))  # Convert to set (automatically removes duplicates)
            print("Your set:", user_set)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please select a number between 1 and 4.")

# Call the menu function to run the program
menu()
