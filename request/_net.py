try:
	from requests import get, post
except ModuleNotFoundError as e:
	print("[ ! ] an error has occured")
	print("[ * ] "+str(e))


class Client( object ):
	def __init__( self ):
		self.url_post_server = "site.com/up.php"
	def write( self, param ):
		r = post( self.url_post_server, data=param, timeout=1000 )
		if r.__contains__(b'uploaded'):
			print("")
		else:
			print("")
