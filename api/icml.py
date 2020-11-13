'''
'''
import urllib.request
from urllib.error import URLError, HTTPError

from bs4 import BeautifulSoup

class ICML(object):
	def __init__(self, year):
		self.year = str(year)
		self.base = f'https://icml.cc/Conferences/' 


	def accepted_papers(self):
		classname = 'maincard narrower Poster'
		posters_url = ''.join([self.base, f'{self.year}/Schedule?type=Poster'])
		resp = urllib.request.urlopen(posters_url)
		soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='iso-8859-1')
		tags = soup.find_all('div', {'class': classname})

		papers = []

		for t in tags: 
			title = t.find('div', {'class', 'maincardBody'}).text
			authors = t.find('div', {'class', 'maincardFooter'}).text
			papers.append({'title': title, 'authors': authors})

		print(papers)
		# return tags
