

class Seat:
    def __init__(self,id, category):
        self.seatId = id
        self.row = None
        self.seatCategory = category

    def getSeatId(self):
        return self.seatId

    def setSeatId(self, seatId):
        self.seatId = seatId

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getSeatCategory(self):
        return self.seatCategory

    def setSeatCategory(self, seatCategory):
        self.seatCategory = seatCategory
