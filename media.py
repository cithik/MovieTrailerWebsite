import webbrowser


class Movie():

    """This class stores movie related information"""

    VALID_RATINGS=["A","B","C","D"]

    def __init__(self,title,storyline,posterimage,trailer_youtube_url):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=posterimage
        self.trailer_youtube_url=trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer)