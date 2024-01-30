class Screen:
    def __init__(self,id, seatslist):
        self.screenId = None
        self.seats = seatslist

    def getScreenId(self):
        return self.screenId

    def setScreenId(self, screenId):
        self.screenId = screenId

    def getSeats(self):
        return self.seats

    def setSeats(self, seats):
        self.seats = seats
