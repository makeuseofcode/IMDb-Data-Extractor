from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# Finding the top movies
top = ia.get_top250_movies()
print(top[0])

# Finding the bottom movies
bottom = ia.get_bottom100_movies()
print(bottom[0])