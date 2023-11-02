class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                row_idx += 1
                

    def search_by_name(self, keyword):
        keyword = keyword.lower()  # Convert keyword to lowercase 
        matching_movies = [movie['name'] for movie in self._movies if keyword in movie['name'].lower()]
        return matching_movies
    
    def search_by_cast(self, keyword):
        keyword = keyword.lower()  # Convert keyword to lowercase for case-insensitive search
        matching_movies = {}
        for movie in self._movies:
            matching_cast = [cast_member for cast_member in movie['cast'] if keyword in cast_member.lower()]
            if matching_cast:
                matching_movies[movie['name']] = matching_cast
        return matching_movies


                

    @property
    def movies(self):
        return self._movies


if __name__ == "__main__":
    movies = Movies('./movies.txt')
