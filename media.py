import webbrowser


class Movie():
    """This class provides a way to store movie related information

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): Title of the movie
        movie_storyline (str): Storyline of the movie
        poster_image (str): Poster image of the movie
        trailer_youtube (str): Trailer of the movie
        release_date (int): Release date of the movie

    Attributes:
        title (str): Title of the movie
        storyline (str): Storyline of the movie
        poster_image_url (str): Poster image of the movie
        trailer_youtube_url (str): Trailer of the movie
        release_date (int): Release date of the movie

    """

    # define instance variables
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        self.title = movie_title                    # title
        self.storyline = movie_storyline            # storyline
        self.poster_image_url = poster_image        # poster image url
        self.trailer_youtube_url = trailer_youtube  # trailor url
        self.release_date = release_date            # release date

    # define instance mthod
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)   # show trailer
