class MovieController:
    def __init__(self):
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie, city):
        self.allMovies.append(movie)

        movies = self.cityVsMovies.get(city, [])
        movies.append(movie)
        self.cityVsMovies[city] = movies

    def getMovieByName(self, movieName):
        for movie in self.allMovies:
            if movie.getMovieName() == movieName:
                return movie
        return None

    def getMoviesByCity(self, city):
        return self.cityVsMovies.get(city)

    #REMOVE movie from a particular city, make use of cityVsMovies map

    #UPDATE movie of a particular city, make use of cityVsMovies map

    #CRUD operation based on Movie ID, make use of allMovies list

    """

class MovieController:
    def __init__(self):
        self.cityVsMovies = {}
        self.allMovies = []

    def addMovie(self, movie, city):
        self.allMovies.append(movie)

        movies = self.cityVsMovies.get(city, [])
        movies.append(movie)
        self.cityVsMovies[city] = movies

    def removeMovie(self, movie, city):
        if city in self.cityVsMovies:
            if movie in self.cityVsMovies[city]:
                self.cityVsMovies[city].remove(movie)

    def updateMovie(self, oldMovie, newMovie, city):
        if city in self.cityVsMovies:
            if oldMovie in self.cityVsMovies[city]:
                index = self.cityVsMovies[city].index(oldMovie)
                self.cityVsMovies[city][index] = newMovie

    def getMovieByName(self, movieName):
        for movie in self.allMovies:
            if movie.getMovieName() == movieName:
                return movie
        return None

    def getMoviesByCity(self, city):
        return self.cityVsMovies.get(city)
"""

    def getMovieById(self, movieId):
        for movie in self.allMovies:
            if movie.getMovieId() == movieId:
                return movie
        return None

    def updateMovieById(self, movieId, newMovie):
        for i, movie in enumerate(self.allMovies):
            if movie.getMovieId() == movieId:
                self.allMovies[i] = newMovie
                break

    def deleteMovieById(self, movieId):
        self.allMovies = [movie for movie in self.allMovies if movie.getMovieId() != movieId]
