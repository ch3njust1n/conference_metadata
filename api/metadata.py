from api.neurips import NeurIPS
from api.icml import ICML
from api.iclr import ICLR

def conference(name, year):
	name = name.lower()

	if name in ['neurips', 'nips']: return NeurIPS(year)
	if name in ['icml']: return ICML(year)
	if name in ['iclr']: return ICLR(year)
	
	return None