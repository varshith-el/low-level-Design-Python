from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def ls(self):
        pass

class Directory(FileSystem):
    def __init__(self, name):
        self.directory_name = name
        self.file_system_list = []

    def add(self, file_system_obj):
        self.file_system_list.append(file_system_obj)

    def ls(self):
        print(f"Directory name {self.directory_name}")
        for file_system_obj in self.file_system_list:
            file_system_obj.ls()

class File(FileSystem):
    def __init__(self, name):
        self.file_name = name

    def ls(self):
        print(f"File name {self.file_name}")


#**main.py**

from directory import Directory
from file import File

def main():
    movie_directory = Directory("Movie")

    border = File("Border")
    movie_directory.add(border)

    comedy_movie_directory = Directory("ComedyMovie")
    hulchul = File("Hulchul")
    comedy_movie_directory.add(hulchul)
    movie_directory.add(comedy_movie_directory)

    movie_directory.ls()

if __name__ == "__main__":
    main()
