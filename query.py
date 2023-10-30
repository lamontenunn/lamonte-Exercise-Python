from movies import Movies

# Instantiating movie_object using the Movies class
movie_object = Movies('./movies.txt')

def menu():
    while True:
        print("\nOptions:")
        print("1: List all movies")
        print("2: Search movies by names")
        print("3: Search movies by cast")
        print("q: Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == 'q':
            break
        elif choice == '1':
            # Listing all movies
            movies = movie_object.movies  # Accessing movies from movie_object
            for movie in movies:
                print(movie['name'])
        elif choice == '2':
            pass 
        elif choice == '3':
            pass  
        else:
            print("Invalid choice. Try again.")

menu()
