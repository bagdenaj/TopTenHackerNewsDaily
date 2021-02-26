import requests
from bs4 import BeautifulSoup
import pprint

def get_rescourse():
	links = []
	subtext = []
	for i in range(1,3):
		res =requests.get(f'https://news.ycombinator.com/news?p={i}')
		soup = BeautifulSoup(res.text, 'html.parser')

		links = links + soup.select('.storylink')
		subtext = subtext + soup.select('.subtext')
		#print(f'https://news.ycombinator.com/news?p={i}')
	return links, subtext

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['points'], reverse=True)

def create_custom_hn():
	links = get_rescourse()[0]
	subtext = get_rescourse()[1]
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().split()[0])
			if points > 100:
				hn.append({'title': title, 'link': href, 'points': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn())