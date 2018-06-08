import webbrowser

class Video():
	"""docstring for Video"""
	def __init__(self,title,duration):
		self.title = title
		self.duration = duration
		

class Movie():
	"""This is the fancy program is used to made for movie things"""
	VALID_RATINGS = ['G','PG','PG-13','R']
	def __init__(self,title,story_line,poster_image,youtube_trailer): #movie_title as title from the class Video (Parent) 
		#self.title = movie_title
		Video.__init__(self,title)
		self.story_line = story_line
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
class Tv(object):
	"""docstring for Tv"""
	def __init__(self,title,duration,season,episode,tv_station):
		Video.__init__(self,title,duration)
		self.season = season
		self.episode = episode
		self.tv_station = tv_station
