class Show:
    def __init__(self,id, screen, movie, showStartTime):
        self.showId = id
        self.movie = movie
        self.screen = screen
        self.showStartTime = showStartTime
        self.bookedSeatIds = []

    def getShowId(self):
        return self.showId

    def setShowId(self, showId):
        self.showId = showId

    def getMovie(self):
        return self.movie

    def setMovie(self, movie):
        self.movie = movie

    def getScreen(self):
        return self.screen

    def setScreen(self, screen):
        self.screen = screen

    def getShowStartTime(self):
        return self.showStartTime

    def setShowStartTime(self, showStartTime):
        self.showStartTime = showStartTime

    def getBookedSeatIds(self):
        return self.bookedSeatIds

    def setBookedSeatIds(self, bookedSeatIds):
        self.bookedSeatIds = bookedSeatIds
