from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# getting movie by IMDb ID
movie = ia.get_movie('0468569')
print(movie)

# printing the names of the directors of the movie
print('Directors:')
for director in movie['directors']:
    print(director['name'])

# printing the genres of the movie
print('Genres:')
for genre in movie['genres']:
    print(genre)