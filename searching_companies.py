from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# Searching for companies having Universal in their names
companies = ia.search_company('Universal')
print(companies)