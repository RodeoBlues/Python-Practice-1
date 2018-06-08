import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
	'A Story of a boy and his toys come to his life',
	'https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg',
	'https://www.youtube.com/watch?v=KYz2wyBy3kc')

# print(toy_story.poster_image_url)

avatar = media.Movie('Avatar',
	'A marine come to an alien planet',
	'https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg',
	'https://www.youtube.com/watch?v=5PSNL1qE6VY')

#print(avatar.story_line)
#avatar.show_trailer()

bolt = media.Movie('Bolt',
	'A story about cute litle Dog',
	'https://en.wikipedia.org/wiki/Bolt_(2008_film)#/media/File:Bolt_ver2.jpg',
	'https://www.youtube.com/watch?v=IBsg00NnzGg')

ratatouile = media.Movie('Ratatouie',
	'A rat is chef in paris',
	'https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg',
	'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in paris',
	'Going back in time to meet authors',
	'https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg',
	'https://www.youtube.com/watch?v=FAfR8omt-CY')

hunger_games = media.Movie('Hunger Games',
	'Real Reality show',
	'https://en.wikipedia.org/wiki/The_Hunger_Games_(film)#/media/File:HungerGamesPoster.jpg',
	'https://www.youtube.com/watch?v=4S9a5V9ODuY')

movies = [toy_story,avatar,bolt,ratatouile,midnight_in_paris,hunger_games]

# fresh_tomatoes.open_movies_page(movies)
# print(bolt.poster_image_url)

# print(media.Movie.VALID_RATINGS	)

hunger_games = media.Movie('Hunger Games',
	'2.00.hr',
	'Real Reality show',
	'https://en.wikipedia.org/wiki/The_Hunger_Games_(film)#/media/File:HungerGamesPoster.jpg',
	'https://www.youtube.com/watch?v=4S9a5V9ODuY')


print(hunger_games.duration)
