'''
'''
import os
import json
import logging
from time import time

'''
Save json data

inputs:
filename (str)  Name of output file
data     (list) JSON object
'''
def save_json(save_dir, filename, data):
	
	if not os.path.isdir(save_dir):
		os.makedirs(save_dir, exist_ok=True)

	with open(os.path.join(save_dir, filename+'.json'), 'w', encoding='utf-8') as file:
		json.dump(data, file, ensure_ascii=False, indent=4)


'''
Clean temp directory
'''
def clean_temp():
    
    files = os.listdir('temp')
    [os.remove(f) for f in files]
    
    
'''
Assumes log file names are formatted as <conference_name><year>-<unix_epoch>.json

inputs:
conference (string) Conference name
year       (year)   Year of the conference
directory  (string) Temp directory path

outputs:
latest_log (string) Filename of the latest log
'''
def get_latest_log(conference, year, directory='temp'):
    
    return sorted([f for f in os.listdir(directory) if f.startswith(f'{conference}{year}')])[-1]
    

'''
'''
def log_level(level):
    level = level.lower()
    
    if level == 'debug':   return logging.DEBUG
    if level == 'info':    return logging.INFO
    if level == 'warning': return logging.WARNING
    if level == 'error':   return logging.ERROR
    if level == 'critcal': return logging.CRITICAL
    
    return ''


'''
Return Unix Epoch time in milliseconds
'''
def unix_epoch():
    decimals = len(str(time()).split('.'))
    return int(time() * 10**decimals)