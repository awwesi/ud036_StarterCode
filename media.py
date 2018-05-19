import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

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
