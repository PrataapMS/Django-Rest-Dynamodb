from NewsAPI.utils import rssfeed_parser


if __name__ == "__main__":
	if len(sys.argv) == 2:
        url = str(sys.argv[1])

	config = {}
	config['url'] = url
	rssfeed_parser(config)