from NewsAPI.utils import rssfeed_parser

if __name__ == "__main__":
	url = ""
	if len(sys.argv) == 2:
		url = str(sys.argv[1])

	config = {}
	if url:
		config['url'] = url
		rssfeed_parser(config)
	else:
		print("mention url")