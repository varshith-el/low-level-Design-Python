# The abstract class for employees and students
class EmployeeAbstract:
    def __init__(self, name, ticket_number, email):
        self.name = name
        self.ticket_number = ticket_number
        self.email = email

    def get_name(self):
        return self.name

    def get_ticket_number(self):
        return self.ticket_number

    def get_email(self):
        return self.email

# The class for employees #TARGET CLASS
class Employee(EmployeeAbstract):
    def __init__(self, name, ticket_number, email, salary):
        super().__init__(name, ticket_number, email)
        self.salary = salary

    def get_salary(self):
        return self.salary

# The class for students #ADAPTEE
class Student:
    def __init__(self, fullname, ticket, email_address, grade):
        # Use different attribute names
        self.fullname = fullname
        self.ticket = ticket
        self.email_address = email_address
        self.grade = grade

    # Define the get methods
    def get_name(self):
        return self.fullname

    def get_ticket_number(self):
        return self.ticket

    def get_email(self):
        return self.email_address

    def get_grade(self):
        return self.grade

# The adapter class for students #ADAPTER
class StudentAdapter(EmployeeAbstract):
    def __init__(self, student):
        # Wrap a student object
        self.student = student

    # Delegate the methods to the student object
    def get_name(self):
        return self.student.get_name()

    def get_ticket_number(self):
        return self.student.get_ticket_number()

    def get_email(self):
        return self.student.get_email()

# The class for passengers #CLIENT.
class Passengers:
    def __init__(self):
        # A list of EmployeeAbstract objects
        self.passengers = []

    def add_passenger(self, passenger):
        # Add an EmployeeAbstract object to the list
        self.passengers.append(passenger)

    def get_passengers(self):
        # Return the list of EmployeeAbstract objects
        return self.passengers

# Create some employee and student objects
employee1 = Employee("Alice", 123, "alice@example.com", 5000)
employee2 = Employee("Bob", 456, "bob@example.com", 6000)
student1 = Student("Charlie", 789, "charlie@example.com", 90)
student2 = Student("David", 101, "david@example.com", 80)

# Create a passengers object
passengers = Passengers()

# Add the employee and student objects to the passengers object
# Use the adapter class to wrap the student objects
passengers.add_passenger(employee1)
passengers.add_passenger(employee2)
passengers.add_passenger(StudentAdapter(student1))
passengers.add_passenger(StudentAdapter(student2))

# Get the list of passengers
passenger_list = passengers.get_passengers()

# Loop through the list and call the get_name method
for passenger in passenger_list:
    print(passenger.get_name())


##############################ANOTHER EXAMPLE###########################################
# "MediaPlayer" is the target class that the client interacts with.
class MediaPlayer:
    def play(self, audio_type, file_name):
        raise NotImplementedError("Subclass must implement abstract method")

# "AdvancedMediaPlayer" is the adaptee class that has specific functionality, but an incompatible interface.
class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        pass

    def play_mp4(self, file_name):
        pass

# "VlcPlayer" and "Mp4Player" are concrete classes implementing "AdvancedMediaPlayer".
class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        return f"Playing vlc file. Name: {file_name}"

class Mp4Player(AdvancedMediaPlayer):
    def play_mp4(self, file_name):
        return f"Playing mp4 file. Name: {file_name}"

# "MediaAdapter" is the adapter class that allows the interface of "AdvancedMediaPlayer" to fit into the "MediaPlayer" interface.
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type.lower() == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_music_player = Mp4Player()

    def play(self, audio_type, file_name):
        if audio_type.lower() == "vlc":
            return self.advanced_music_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            return self.advanced_music_player.play_mp4(file_name)

# "AudioPlayer" is the client class that interacts with the "MediaPlayer" interface.
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        # Inbuilt support to play mp3 music files
        if audio_type.lower() == "mp3":
            return f"Playing mp3 file. Name: {file_name}"
        # MediaAdapter is providing support to play other file formats
        elif audio_type.lower() in ["vlc", "mp4"]:
            media_adapter = MediaAdapter(audio_type)
            return media_adapter.play(audio_type, file_name)
        else:
            return f"Invalid media. {audio_type} format not supported"

# Let's test our code:
if __name__ == "__main__":
    audio_player = AudioPlayer()
    print(audio_player.play("mp3", "beyond the horizon.mp3"))
    print(audio_player.play("mp4", "alone.mp4"))
    print(audio_player.play("vlc", "far far away.vlc"))
    print(audio_player.play("avi", "mind me.avi"))
