from api.neurips import NeurIPS
from api.icml import ICML

def conference(name, year):
	name = name.lower()

	if name in ['neurips', 'nips']: return NeurIPS(year)
	if name in ['icml']: return ICML(year)
	
	return None