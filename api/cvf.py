'''
'''
import os
import re
import sys
import json
import logging
import urllib.request
from collections import defaultdict
from tqdm import tqdm
from pprint import pprint

import api.utils as utils
from bs4 import BeautifulSoup, Tag
from api.batcher import batch_process

class CVF(object):
	def __init__(self, year, logname):
		self.year = str(year)
		self.base = f'https://openaccess.thecvf.com' 
		self.failed = defaultdict(list)
		self.log = logging.getLogger(logname)
		self.workshop = f'https://openaccess.thecvf.com/CVPR2022_workshops/menu'


	'''
 	'''
	def capitalize_hyphenated(self, name):
		return ('-'.join([i.capitalize() for i in name.split('-')])).title()


	'''
	Format authors list

	inputs:
	authors (str) Author names separated by commas

	outputs:
	authors (list) List of dicts of author information
	'''
	def format_auths(self, authors):
		res = []

		for a in authors.split(','):
			a = a.strip().split()
			res.append({
				'given_name': self.capitalize_hyphenated(' '.join(a[:-1]).capitalize()),
				'family_name': self.capitalize_hyphenated(a[-1]).title() if len(a) > 1 else '',
				'institution': None
			})

		return res


	def build_proceedings_list(self, kw):
		resp = urllib.request.urlopen('https://openaccess.thecvf.com/menu')
		soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='utf-8')
		tags = soup.find_all('div', {'id': 'content'})[0].find_all('dd')
		
		proceedings = []

		for t in tags:
			title = t.text.strip().split(',')[0]
			if kw.lower() in title.lower(): proceedings.append((title, re.search(r'\d{4}', title).group()))	
		
		return proceedings


	def extract_papers(self, page):
		soup = BeautifulSoup(page.read(), 'html.parser', from_encoding='utf-8')
		count = 0
		proceedings = []
		paper = defaultdict()

		for tag in soup.find('dl').children:
			if isinstance(tag, Tag):
				if tag.find_all('a')[0].text.lower() == 'back': 
					continue
				else:
					count = count % 3 + 1
					
					if count == 1:
						paper = defaultdict()
						paper["title"] = tag.text
					elif count == 2:
						authors = []
						
						for auth in tag.find_all('a'):
							auth = auth.text.split()
							authors.append({
								"given_name": ' '.join(auth[:-1]),
								"family_name": auth[-1],
								"institution": ''
							})

						paper["authors"] = authors
					elif count == 3:
						paper["url"] = [f"{self.base}{link['href']}" for link in tag.find_all('a', href=True) if link['href'].endswith('.pdf') and link['href'].startswith('/content')]
						proceedings.append(paper)

		return proceedings

		
	
	def accepted_papers(self, use_checkpoint=True, kw='cvpr'):
		proceedings = self.build_proceedings_list(kw=kw)
		print(proceedings)
		is_sorted_by_days = lambda html: any('day=' in tag['href'] for tag in html.find_all('a'))

		for conf, year in proceedings:
			conf_url =f"{self.base}/{conf.replace(' ','')}"
			page = urllib.request.urlopen(conf_url)
			soup = BeautifulSoup(page.read(), 'html.parser', from_encoding='utf-8')
			papers = []

			if is_sorted_by_days(soup):
				papers = self.extract_papers(urllib.request.urlopen(conf_url+'?day=all'))
				pprint(papers)
				pass
			else:
				pass

			utils.save_json(f'./{kw}', f'{kw}_{year}', papers)

			break