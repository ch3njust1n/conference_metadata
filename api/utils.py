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
