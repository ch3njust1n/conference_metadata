'''
'''
import os
import configparser

import api.metadata as md
import api.utils as utils


def main():
	config = configparser.ConfigParser(allow_no_value=True)
	config.read('config.ini')
	cfg = config['DEFAULT']

	name = cfg['conference']
	year = cfg['year']
	save_dir = cfg['save_dir']

	if not os.path.isdir(save_dir):
		os.makedirs(save_dir, exist_ok=True) 

	metadata = md.conference(name, year).accepted_papers()
	utils.save_json(save_dir, f'{name}_{year}', metadata)
	

if __name__ == '__main__':
	main()