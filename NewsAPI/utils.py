import feedparser
'''
Rssfeed parser
input:
config = {'url':"url"}
'''
def get_search_dict():
		return {}

def rssfeed_parser(config=None):
    if config:
        url = config.get('url', None)
        if url:
        	fp = feedparser.parse(url)
        	return fp.entries
    return None
        	
def classify_newspost(post=""):
		search_dict = get_search_dict()
		print search_dict
        