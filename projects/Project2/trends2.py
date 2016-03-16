
"""Visualizing Twitter Sentiment Across America"""

from data import word_sentiments, load_tweets
from datetime import datetime
from geo import us_states, geo_distance, make_position, longitude, latitude
from maps import draw_state, draw_name, draw_dot, wait
from string import ascii_letters
from ucb import main, trace, interact, log_current_line


###################################
# Phase 1: The Feelings in Tweets #
###################################

# Q1
# The tweet abstract data type, implemented as a dictionary.

def make_tweet(text, time, lat, lon):
	"""Return a tweet, represented as a Python dictionary.

	text  -- A string; the text of the tweet, all in lowercase
	time  -- A datetime object; the time that the tweet was posted
	lat   -- A number; the latitude of the tweet's location
	lon   -- A number; the longitude of the tweet's location

	>>> t = make_tweet("just ate lunch", datetime(2012, 9, 24, 13), 38, 74)
	>>> tweet_text(t)
	'just ate lunch'
	>>> tweet_time(t)
	datetime.datetime(2012, 9, 24, 13, 0)
	>>> p = tweet_location(t)
	>>> latitude(p)
	38
	>>> tweet_string(t)
	'"just ate lunch" @ (38, 74)'
	"""
	return {'text': text, 'time': time, 'latitude': lat, 'longitude': lon}

def tweet_text(tweet):
	"""Return a string, the words in the text of a tweet."""
	return tweet['text']

def tweet_time(tweet):
	"""Return the datetime representing when a tweet was posted."""
	return tweet['time']

def tweet_location(tweet): #makes position
	"""Return a position representing a tweet's location."""
	return make_position(tweet['latitude'],tweet['longitude']) #makes position object

# The tweet abstract data type, implemented as a function.

def make_tweet_fn(text, time, lat, lon):
	"""An alternate implementation of make_tweet: a tweet is a function.

	>>> t = make_tweet_fn("just ate lunch", datetime(2012, 9, 24, 13), 38, 74)
	>>> tweet_text_fn(t)
	'just ate lunch'
	>>> tweet_time_fn(t)
	datetime.datetime(2012, 9, 24, 13, 0)
	>>> latitude(tweet_location_fn(t))
	38
	"""
	tweet_dictionary = {'text':  text, 'time': time, 'lat': lat, 'lon': lon}
	def lookup(key):
		return tweet_dictionary[key]
	return lookup

def tweet_text_fn(tweet):
	"""Return a string, the words in the text of a functional tweet."""
	return tweet('text')

def tweet_time_fn(tweet):
	"""Return the datetime representing when a functional tweet was posted."""
	return tweet('time')

def tweet_location_fn(tweet):
	"""Return a position representing a functional tweet's location."""
	return make_position(tweet('lat'), tweet('lon'))

### === +++ ABSTRACTION BARRIER +++ === ###

def tweet_words(tweet):
	"""Return the words in a tweet."""
	return extract_words(tweet_text(tweet))

def tweet_string(tweet):
	"""Return a string representing a functional tweet."""
	location = tweet_location(tweet)
	point = (latitude(location), longitude(location))
	return '"{0}" @ {1}'.format(tweet_text(tweet), point)

# Q2

def extract_words(text):
	"""Return the words in a tweet, not including punctuation.

	>>> extract_words('anything else.....not my job')
	['anything', 'else', 'not', 'my', 'job']
	>>> extract_words('i love my job. #winning')
	['i', 'love', 'my', 'job', 'winning']
	>>> extract_words('make justin # 1 by tweeting #vma #justinbieber :)')
	['make', 'justin', 'by', 'tweeting', 'vma', 'justinbieber']
	>>> extract_words("paperclips! they're so awesome, cool, & useful!")
	['paperclips', 'they', 're', 'so', 'awesome', 'cool', 'useful']
	>>> extract_words('@(cat$.on^#$my&@keyboard***@#*')
	['cat', 'on', 'my', 'keyboard']
	"""
	n = ""
	for char in text:
		n += char if char in ascii_letters else " "
	return n.split()

# Q3

def make_sentiment(value):
	"""Return a sentiment, which represents a value that may not exist.

	>>> positive = make_sentiment(0.2)
	>>> neutral = make_sentiment(0)
	>>> unknown = make_sentiment(None)
	>>> has_sentiment(positive)
	True
	>>> has_sentiment(neutral)
	True
	>>> has_sentiment(unknown)
	False
	>>> sentiment_value(positive)
	0.2
	>>> sentiment_value(neutral)
	0
	"""
	assert value is None or (value >= -1 and value <= 1), 'Illegal value'
	return value

def has_sentiment(s):
	"""Return whether sentiment s has a value."""
	return s is not None

def sentiment_value(s):
	"""Return the value of a sentiment s."""
	assert has_sentiment(s), 'No sentiment value'
	return s

def get_word_sentiment(word):
	"""Return a sentiment representing the degree of positive or negative
	feeling in the given word.

	>>> sentiment_value(get_word_sentiment('good'))
	0.875
	>>> sentiment_value(get_word_sentiment('bad'))
	-0.625
	>>> sentiment_value(get_word_sentiment('winning'))
	0.5
	>>> has_sentiment(get_word_sentiment('Berkeley'))
	False
	"""
	# Learn more: http://docs.python.org/3/library/stdtypes.html#dict.get
	return make_sentiment(word_sentiments.get(word))

# Q4

def analyze_tweet_sentiment(tweet):
	""" Return a sentiment representing the degree of positive or negative
	sentiment in the given tweet, averaging over all the words in the tweet
	that have a sentiment value.

	If no words in the tweet have a sentiment value, return
	make_sentiment(None).

	>>> positive = make_tweet('i love my job. #winning', None, 0, 0)
	>>> round(sentiment_value(analyze_tweet_sentiment(positive)), 5)
	0.29167
	>>> negative = make_tweet("saying, 'i hate my job'", None, 0, 0)
	>>> sentiment_value(analyze_tweet_sentiment(negative))
	-0.25
	>>> no_sentiment = make_tweet("berkeley golden bears!", None, 0, 0)
	>>> has_sentiment(analyze_tweet_sentiment(no_sentiment))
	False
	"""
	average, words_with_sent = make_sentiment(None), 0
	for word in tweet_words(tweet):
		sentiment = get_word_sentiment(word)
		if has_sentiment(average) and has_sentiment(sentiment):
			average = make_sentiment(sentiment_value(sentiment) +
				sentiment_value(average))
			words_with_sent += 1
		elif not has_sentiment(average) and has_sentiment(sentiment):
			average = make_sentiment(sentiment_value(sentiment))
			words_with_sent += 1
		# else both average and sentiment have no sentiment value
		# and remain None
	if words_with_sent == 0:
		return average
	return make_sentiment(sentiment_value(average) / words_with_sent)

# Q5

def find_centroid(polygon):
	"""Find the centroid of a polygon.

	http://en.wikipedia.org/wiki/Centroid#Centroid_of_polygon

	polygon -- A list of positions, in which the first and last are the same

	Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area

	Hint: If a polygon has 0 area, use the latitude and longitude of its first
	position as its centroid.

	>>> p1, p2, p3 = make_position(1, 2), make_position(3, 4), make_position(5, 0)
	>>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
	>>> round5 = lambda x: round(x, 5) # Rounds floats to 5 digits
	>>> tuple(map(round5, find_centroid(triangle)))
	(3.0, 2.0, 6.0)
	>>> tuple(map(round5, find_centroid([p1, p3, p2, p1])))
	(3.0, 2.0, 6.0)
	>>> tuple(map(float, find_centroid([p1, p2, p1])))  # A zero-area polygon
	(1.0, 2.0, 0.0)
	"""
	area, cent_lat, cent_lon = 0, 0, 0
	for i in range(len(polygon) - 1):
		x1, y1 = latitude(polygon[i]), longitude(polygon[i])
		x2, y2 = latitude(polygon[i+1]), longitude(polygon[i+1])
		area += .5 * (x1*y2 - x2*y1)
		cent_lat += (x1+x2) * (x1*y2 - x2*y1)
		cent_lon += (y1+y2) * (x1*y2 - x2*y1)
	if area == 0:
		return latitude(polygon[0]), longitude(polygon[0]), area
	return cent_lat / (6*area), cent_lon / (6*area), abs(area)

# Q6

def find_state_center(polygons):
	"""Compute the geographic center of a state, averaged over its polygons.

	The center is the average position of centroids of the polygons in polygons,
	weighted by the area of those polygons.

	Arguments:
	polygons -- a list of polygons

	>>> ca = find_state_center(us_states['CA'])  # California
	>>> round(latitude(ca), 5)
	37.25389
	>>> round(longitude(ca), 5)
	-119.61439

	>>> hi = find_state_center(us_states['HI'])  # Hawaii
	>>> round(latitude(hi), 5)
	20.1489
	>>> round(longitude(hi), 5)
	-156.21763
	"""
	cent_lat_num, cent_lon_num, sum_areas = 0, 0, 0
	for i in range(len(polygons)):
		lat, lon, area = find_centroid(polygons[i])
		cent_lat_num += (lat * area)
		cent_lon_num += (lon * area)
		sum_areas += area
	return make_position(cent_lat_num / sum_areas, cent_lon_num / sum_areas)

# Q7

def get_state_centers():
	"""Helper function that returns a dictionary of all states and their centroids
	"""
	return {n: find_state_center(s) for n, s in us_states.items()}

# global instance, so it doesn't have to be calculated every time
us_centers = get_state_centers()

###################################
# Phase 3: The Mood of the Nation #
###################################

def group_tweets_by_state(tweets):
	"""Return a dictionary that aggregates tweets by their nearest state center.

	The keys of the returned dictionary are state names, and the values are
	lists of tweets that appear closer to that state center than any other.

	tweets -- a sequence of tweet abstract data types

	>>> sf = make_tweet("welcome to san francisco", None, 38, -122)
	>>> ny = make_tweet("welcome to new york", None, 41, -74)
	>>> two_tweets_by_state = group_tweets_by_state([sf, ny])
	>>> len(two_tweets_by_state)
	2
	>>> california_tweets = two_tweets_by_state['CA']
	>>> len(california_tweets)
	1
	>>> tweet_string(california_tweets[0])
	'"welcome to san francisco" @ (38, -122)'
	""" 
	def nearest_state(tweet_pos):
		"""Calculates the closest state given the position of a tweet,
		and returns the key for that state.
		"""
		closest_state, dist = "", None
		for state in us_states:
			this_dist = geo_distance(tweet_pos, us_centers[state])
			if dist is None or this_dist < dist:
				dist = this_dist
				closest_state = state
		return closest_state 

	tweets_by_state = {}
	for tweet in tweets:
		closest = nearest_state(tweet_location(tweet))
		if closest not in tweets_by_state:
			tweets_by_state[closest] = [tweet]
		else:
			tweets_by_state[closest] += [tweet]
	return tweets_by_state

# Q8

def average_sentiments(tweets_by_state):
	"""Calculate the average sentiment of the states by averaging over all
	the tweets from each state. Return the result as a dictionary from state
	names to average sentiment values (numbers).

	If a state has no tweets with sentiment values, leave it out of the
	dictionary entirely.  Do NOT include states with no tweets, or with tweets
	that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
	sentiment.

	tweets_by_state -- A dictionary from state names to lists of tweets
	"""
	averaged_state_sentiments = {}
	for state, tweets in tweets_by_state:
		count, total_sent, this_sent = 0, 0, 0
		for tweet in tweets:
			this_sent += analyze_tweet_sentiment(tweet)
			if has_sentiment(this_sent):
				count += 1
				total_sent += sentiment_value(this_sent)
		if count > 0:
			averaged_state_sentiments[state] = make_sentiment(total_sent / count)
	return averaged_state_sentiments