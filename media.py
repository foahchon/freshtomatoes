import webbrowser

class Movie():

    """The Movie class stores information about a given movie.
    
    Attributes:
        title: The movie's title.
        year: Year of the movie's release.
        storyline: A brief storyline summary or synopsis.
        poster_image_url: A URL referencing an image of the movie's theatrical
            poster.
        trailer_youtube_url: A URL referencing an image of the movie's 
            theatrical trailer on YouTube.

        """

    def __init__(self, movie_title, movie_year, movie_storyline,
                 poster_image, trailer_youtube):

        """Args:
            movie_title: Movie's title.
            movie_year: Year of movie's release.
            movie_storyline: Movie's synopsis.
            poster_image: A URL referencing the movie's poster.
            trailer_youtube: A URL referencing the movie's trailer on YouTube.

        """

        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):

        """Displays movie's trailer in a web browser."""

        webbrowser.open(self.trailer_youtube_url)