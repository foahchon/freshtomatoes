import webbrowser

class Movie():

    # class includes fields for title, year of release, storyline (synopsis), poster URL, and a YouTube URL for the film's trailer
    def __init__(self, movie_title, movie_year, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) # open trailer in web browser