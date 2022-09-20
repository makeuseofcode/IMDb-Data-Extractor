from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# Searching movies that have rock in their name
movies = ia.search_movie('rock')
print(movies[0])