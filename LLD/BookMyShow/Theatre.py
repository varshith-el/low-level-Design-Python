
class Theatre:
    def __init__(self,id, screenlist,city,shows):
        self.theatreId = id
        self.address = None
        self.city = city
        self.screen = screenlist
        self.shows = shows

    def getTheatreId(self):
        return self.theatreId

    def setTheatreId(self, theatreId):
        self.theatreId = theatreId

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getScreen(self):
        return self.screen

    def setScreen(self, screen):
        self.screen = screen

    def getShows(self):
        return self.shows

    def setShows(self, shows):
        self.shows = shows

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city
