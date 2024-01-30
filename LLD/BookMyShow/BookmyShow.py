from typing import List
from Screen import Screen
from MovieController import MovieController
from Theatre import Theatre
from Show import Show
from Booking import Booking
from TheatreController import TheatreController
from Movie import Movie
from Seat import Seat
from Enums.SeatCategory import SeatCategory
from Enums.City import City

class BookMyShow:
    def __init__(self):
        self.movieController = MovieController()
        self.theatreController = TheatreController()

    def createBooking(self, userCity, movieName):
        # 1. search movie by my location
        movies = self.movieController.getMoviesByCity(userCity)

        # 2. select the movie which you want to see. i want to see Baahubali
        interestedMovie = None
        for movie in movies:
            if movie.getMovieName() == movieName:
                interestedMovie = movie

        # 3. get all show of this movie in Bangalore location
        showsTheatreWise = self.theatreController.getAllShow(interestedMovie, userCity)

        # 4. select the particular show user is interested in
        entry = next(iter(showsTheatreWise.items()))
        runningShows = entry[1]
        interestedShow = runningShows[0]

        # 5. select the seat
        seatNumber = 30
        bookedSeats = interestedShow.getBookedSeatIds()
        if seatNumber not in bookedSeats:
            bookedSeats.append(seatNumber)
            # startPayment
            booking = Booking()
            myBookedSeats = []
            for screenSeat in interestedShow.getScreen().getSeats():
                if screenSeat.getSeatId() == seatNumber:
                    myBookedSeats.append(screenSeat)
            booking.setBookedSeats(myBookedSeats)
            booking.setShow(interestedShow)
        else:
            # throw exception
            print("seat already booked, try again")
            return

        print("BOOKING SUCCESSFUL")

    def initialize(self):
        # create movies
        self.createMovies()

        # create theater with screens, seats and shows
        self.createTheatre()

    def createTheatre(self):
        # Logic for creating a theatre
        avengerMovie = self.movieController.getMovieByName("AVENGERS")
        baahubali = self.movieController.getMovieByName("BAAHUBALI")

        inoxTheatre = Theatre(1, self.createScreen(), City.Bangalore, [])
        inoxShows = [self.createShows(1, inoxTheatre.getScreen()[0], avengerMovie, 8), 
                     self.createShows(2, inoxTheatre.getScreen()[0], baahubali, 16)]
        inoxTheatre.setShows(inoxShows)

        pvrTheatre = Theatre(2, self.createScreen(), City.Delhi, [])
        pvrShows = [self.createShows(3, pvrTheatre.getScreen()[0], avengerMovie, 13), 
                    self.createShows(4, pvrTheatre.getScreen()[0], baahubali, 20)]
        pvrTheatre.setShows(pvrShows)

        self.theatreController.addTheatre(inoxTheatre, City.Bangalore)
        self.theatreController.addTheatre(pvrTheatre, City.Delhi)

    def createScreen(self) -> List[Screen]:
        # Logic for creating a screen
        screen1 = Screen(1, self.createSeats())
        return [screen1]

    def createShows(self, showId, screen, movie, showStartTime) -> Show:
        # Logic for creating a show
        return Show(showId, screen, movie, showStartTime)

    def createSeats(self) -> List[Seat]:
        # Logic for creating seats
        seats = []
        for i in range(100):
            if i < 40:
                seats.append(Seat(i, SeatCategory.SILVER))
            elif i < 70:
                seats.append(Seat(i, SeatCategory.GOLD))
            else:
                seats.append(Seat(i, SeatCategory.PLATINUM))
        return seats

    def createMovies(self):
        # Logic for creating movies
        avengers = Movie(1, "AVENGERS", 128)
        baahubali = Movie(2, "BAAHUBALI", 180)

        self.movieController.addMovie(avengers, City.Bangalore)
        self.movieController.addMovie(avengers, City.Delhi)
        self.movieController.addMovie(baahubali, City.Bangalore)
        self.movieController.addMovie(baahubali, City.Delhi)

if __name__ == "__main__":
    bookMyShow = BookMyShow()
    bookMyShow.initialize()
    bookMyShow.createBooking(City.Bangalore, "BAAHUBALI")
    
    bookMyShow.createBooking(City.Bangalore, "BAAHUBALI")



#Credits:SJ