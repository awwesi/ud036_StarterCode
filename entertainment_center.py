import media
import fresh_tomatoes


# instance of class Movie
goodfellas = media.Movie("Goodfellas",
                         "A story about the life in the Mafia",
                         "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y",
                         1990)

# instance of class Movie
the_big_lebowski = media.Movie("The Big Lebowski",
                               "A story about a Los Angeles slacker and avid bowler.",  # NOQA
                               "http://img.moviepostershop.com/the-big-lebowski-movie-poster-1998-1010196337.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=ngV0RBhGZmE",
                               1998)

# instance of class Movie
a_fish_called_wanda = media.Movie("A Fish Called Wanda",
                                  "A story about a gang of diamond thieves who double-cross one another to find stolen diamonds hidden by the gang leader.",  # NOQA
                                  "https://image.tmdb.org/t/p/w220_and_h330_bestv2/hkSGFNVfEEUXFCxRZDITFHVhUlu.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=dqAJUlSRCwo",  # NOQA
                                  1988)
# instance of class Movie
when_harry_met_sally = media.Movie("When Harry Met Sally",
                                   "The story follows the title characters from the time they meet just before sharing a cross-country drive, through twelve years of chance encounters in New York City.",  # NOQA
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/1/1c/WhenHarryMetSallyPoster.jpg/220px-WhenHarryMetSallyPoster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=V8DgDmUHVto",  # NOQA
                                   1989)

# instance of class Movie
titanic = media.Movie("Titanic",
                      "The story of Titanic with two play characters who are of different social classes. ",  # NOQA
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
                      1997)

# instance of class Movie
wall_street = media.Movie("Wall Street",
                          "A story about a corrupt and greedy stockbroker",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Wall_Street_film.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=evRhOcqnAHc",
                          1987)

# create a list of instances of class Movie
movies = [goodfellas, the_big_lebowski, a_fish_called_wanda,
          when_harry_met_sally, titanic, wall_street]

# open the website with the parameter of the movies list
fresh_tomatoes.open_movies_page(movies)
