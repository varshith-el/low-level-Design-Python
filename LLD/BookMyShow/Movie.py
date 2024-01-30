class Movie:
    def __init__(self,id, name, dur):
        self.movieId = id
        self.movieName = name
        self.movieDurationInMinutes = dur
        #other details like Genere, Language etc.

    def getMovieId(self):
        return self.movieId

    def setMovieId(self, movieId):
        self.movieId = movieId

    def getMovieName(self):
        return self.movieName

    def setMovieName(self, movieName):
        self.movieName = movieName

    def getMovieDuration(self):
        return self.movieDurationInMinutes

    def setMovieDuration(self, movieDuration):
        self.movieDurationInMinutes = movieDuration
