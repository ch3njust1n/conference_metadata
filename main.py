'''
'''
import os
import logging
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
	log_level = cfg['log_level']
 
	if not os.path.isdir(save_dir):
		os.makedirs(save_dir, exist_ok=True) 
  
	if not os.path.isdir('temp') or not os.path.isdir('temp/failed'):
		os.makedirs('temp/failed', exist_ok=True)
  
	if not os.path.isdir('logs'):
		os.makedirs('logs', exist_ok=True)
  
	logname = f'logs/{name}{year}-{utils.unix_epoch()}.log'
 
	print(f'log file: {logname}')
  
	logging.basicConfig(
     	level=utils.log_level(log_level), 
    	filename=logname,
     	filemode='w', 
      	format='%(name)s - %(levelname)s - %(message)s'
    )

	metadata = md.conference(name, year, logname).accepted_papers()
	utils.save_json(save_dir, f'{name}_{year}', metadata)
 
	print('total time: ', time() - start_time)
	

if __name__ == '__main__':
	main()