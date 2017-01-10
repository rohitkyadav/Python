from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'muUFLJfDsee97d6Alsknuacji'
csecret = 'or4K3BCzno91tBFPqPisBUOc7YUykXlRhaeUi9Nel7sbtctZyj'
atoken = '764053684305166336-WFOvCBiC8cf0vfHpTEI3ID4VtPW9ENi'
asecret = '1m64ccpdDvSE5MrcnDbdV1s7EC09kJalKWYMycCC2dI74'

class listener(StreamListener):
	def on_data(self, data):
		print (data)
		return True
	def on_error(self, status):
		print(status)

auth = OAuthHandler (ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["movie"])