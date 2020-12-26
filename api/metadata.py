from api.neurips import NeurIPS
from api.icml import ICML
from api.iclr import ICLR
from api.acl import *

def conference(name, year):
	name = name.lower()

	if name in ['neurips', 'nips']: return NeurIPS(year)
	if name in ['icml']: return ICML(year)
	if name in ['iclr']: return ICLR(year)
	# convert string to class object as in datapipe
	
	return None