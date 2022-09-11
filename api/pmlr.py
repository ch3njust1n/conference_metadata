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

import api.utils as utils
from bs4 import BeautifulSoup
from api.batcher import batch_process

class PMLR(object):
	def __init__(self, year, logname):
		self.year = str(year)
		self.base = f'https://proceedings.mlr.press/' 
		self.failed = defaultdict(list)
		self.log = logging.getLogger(logname)


	def build_proceedings(self):
		resp = urllib.request.urlopen(self.base)
		soup = BeautifulSoup(resp.read(), 'html.parser', from_encoding='utf-8')
		tags = soup.find_all('ul', {'class': 'proceedings-list'})

		print(tags)
		
	
	def accepted_papers(self, use_checkpoint=True):
		self.build_proceedings()
  