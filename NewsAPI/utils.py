import feedparser
'''
Rssfeed parser
input:
config = {'url':"url"}
'''
def rssfeed_parser(config=None):
    if config:
        url = config.get('url', None)
        if url:
        	print("Hello12345")
        	# fp = feedparser.parse(url)
        	return fp.entries
    return None
        	
def classify_new(post=""):
		search_dict = get_search_dict()
