'''
'''
import re
import urllib.request
from urllib.error import URLError, HTTPError

from bs4 import BeautifulSoup

class ICML(object):
	def __init__(self, year):
		self.year = str(year)
		self.base = f'https://icml.cc/Conferences/' 


	def get_institutions(self, eventID):
		event_url = 'https://icml.cc/Conferences/2021/Schedule?showEvent={eventID}'
		resp = urllib.request.urlopen(event_url)
		soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='iso-8859-1')
		tags = soup.find_all('button', {'class': 'btn btn-default'})

		print(soup)

		def get_institution(_id):
			print(_id)
			speaker_url = 'https://icml.cc/Conferences/2021/Schedule?showSpeaker={_id}'
			resp = urllib.request.urlopen(speaker_url)
			soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='iso-8859-1')
			tags = soup.find_all('button', {'class': 'maincard Remark col-sm-12'})

			print(tags)
			# return tags

		# src: https://stackoverflow.com/a/50122731/3158028
		exp = '(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?'
		institutions = [get_institution(re.search(exp, t.get('onclick'))) for t in tags]
		


	'''
	Format authors list

	inputs:
	authors (str) Author names separated by commas

	outputs:
	authors (list) List of dicts of author information
	'''
	def format_auths(self, authors):
		res = []

		for a in authors.split('·'):
			a = a.split()
			res.append({
				'given_name': ''.join(a[:-1]),
				'family_name': a[-1] if len(a) > 1 else '',
				'institution': None
			})

		return res


	def accepted_papers(self):
		classname = 'maincard narrower poster'
		posters_url = ''.join([self.base, f'{self.year}/Schedule?type=Poster'])
		resp = urllib.request.urlopen(posters_url)
		soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='iso-8859-1')
		tags = soup.find_all('div', {'class': classname})

		papers = []

		for t in tags: 
			tag_id = t.get('id').split('_')[-1]
			title = t.find('div', {'class', 'maincardBody'}).text
			authors = t.find('div', {'class', 'maincardFooter'}).text
			papers.append({'id': tag_id, 'title': title, 'authors': self.format_auths(authors)})

		print(papers[0])
		self.get_institutions(papers[0]['id'])
		return papers