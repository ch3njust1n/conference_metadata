'''
'''

class ICLR(object):
	def __init__(self, year):
		self.year = year
		self.base = 
		self.proceedings = {
			'2013': 'https://iclr.cc/archive/2013/conference-proceedings.html',
			'2014': 'https://iclr.cc/archive/2014/conference-proceedings/',
			'2015': 'https://iclr.cc/archive/www/doku.php%3Fid=iclr2015:accepted-main.html',
			'2016': 'https://iclr.cc/archive/www/doku.php%3Fid=iclr2016:accepted-main.html',
			'2017': 'https://iclr.cc/archive/www/doku.php%3Fid=iclr2017:conference_posters.html',
			'2018': {
				'poster': 'https://openreview.net/group?id=ICLR.cc/2018/Conference',
				'workshop': 'https://openreview.net/group?id=ICLR.cc/2018/Workshop'
			},
			'2019': {
				'poster': 'https://openreview.net/group?id=ICLR.cc/2018/Conference',
				'workshop': 'https://openreview.net/group?id=ICLR.cc/2018/Workshop'
			},
		
		}