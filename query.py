def menu():
    while True:
        print("Options:")
        print("1: List all movies")
        print("2: Search movies by names")
        print("3: Search movies by cast")
        print("q: Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == 'q' or choice == 'Q':
            break
        elif choice == '1':
            pass  # Code for listing all movies 
        elif choice == '2':
            pass  # Code for searching movies by names 
        elif choice == '3':
            pass  # Code for searching movies by cast
        else:
            print("Invalid choice. Try again.")


menu()
