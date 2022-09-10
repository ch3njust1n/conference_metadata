'''
'''
import os
import configparser
from time import time

import api.metadata as md
import api.utils as utils


def main():
	start_time = time()
	config = configparser.ConfigParser(allow_no_value=True)
	config.read('config.ini')
	cfg = config['DEFAULT']

	name = cfg['conference']
	year = cfg['year']
	save_dir = cfg['save_dir']

	if not os.path.isdir(save_dir):
		os.makedirs(save_dir, exist_ok=True) 
  
	if not os.path.isdir('temp'):
		os.makedirs('temp', exist_ok=True)

	metadata = md.conference(name, year).accepted_papers()
	utils.save_json(save_dir, f'{name}_{year}', metadata)
 
	print('total time: ', time() - start_time)
	

if __name__ == '__main__':
	main()