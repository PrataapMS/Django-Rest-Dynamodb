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
        	fp = feedparser.parse(url)
        	print (fp)
        	
