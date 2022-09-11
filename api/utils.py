'''
'''
import os
import json

'''
Save json data

inputs:
filename (str)  Name of output file
data     (list) JSON object
'''
def save_json(save_dir, filename, data):

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
    