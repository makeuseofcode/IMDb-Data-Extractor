from imdb import Cinemagoer

# Creating an instance of the Cinemagoer class
ia = Cinemagoer()

# getting person data by ID
person = ia.get_person('0005132')
print(person['name'])
print(person['birth date'])

# getting company data by ID
company = ia.get_company('0005073')
print(company['name'])