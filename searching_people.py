from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# Searching for people having Heath in their names
persons = ia.search_person('Heath')
print(persons[0])