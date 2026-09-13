current_movies  = {'The Grinch': '11:00 AM',
                   'Rudolph': '2:00 PM',
                   'Frosty the Snowman': '5:00 PM',
                   'A Charlie Brown Christmas': '8:00 PM'}
print("Current movies playing: ")
for movie in current_movies:
    print(movie)
input_movie = input("What movie would you like the showtimes for? \n")
showtime = current_movies.get(input_movie)
if showtime:
    print(f"The showtime for {input_movie} is {showtime}.")
else:
    print("Movie not found.")
