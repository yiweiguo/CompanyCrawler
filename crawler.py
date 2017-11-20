from openpyxl import load_workbook
from FullContact import FullContact
import json
import requests

ACCESS_TOKEN = '58188b712e32cd16'

class FullContact(object):
	def __init__(self, api_key):
		self.api_key = api_key
		self.base_url = 'https://api.fullcontact.com/v2/'
		self.get_endpoints = {
			'person': 'person.json',
			'company_search': 'company/search.json'
		}
		self.post_endpoints = {
            'batch': 'batch.json'
        }
		for endpoint in self.get_endpoints:
			# method that will invoke the self.api_get
			method = lambda endpoint = endpoint, **kwargs: self.api_get(endpoint, **kwargs)
			# set the end_point to be a method() callable
			setattr(self, endpoint, method)


	def api_get(self, endpoint, **kwargs):
		headers = {'X-FullContact-APIKey': self.api_key}
		endpoint = self.base_url + self.get_endpoints[endpoint]
		return requests.get(endpoint, params=kwargs, headers=headers)

def load_data(filename):
	'''
	Grab the data in the A1 column and stores it to
	a List 
	parameters: filename -- name of the file xlsx to be read
	return: list that contains all the name in string from the first column
	'''
	names = []
	wb2 = load_workbook(filename)
	# get the active worksheet
	ws = wb2.active 
	cells_dict = ws._cells
	for c in cells_dict.keys():
		# (row, column) as keys
		if (c[1] == 1):
			names.append(cells_dict[c].value)
	assert(len(names) <= len(cells_dict))
	return names

def get_info_dict(names):
	'''
	get the company name and info hash 
	parameters:
	names: names of the company in a list
	return:
	{company_name: json file of the company}
	'''
	info_dict = {}
	fc = FullContact(ACCESS_TOKEN)
	for name in names: 
		print(name)
		# calls are made in a small window
		info_dict[name] = fc.company_search(companyName=name)
		sleep(0.5)
	return info_dict

def main():	
	filename = 'Financial_company _UNlist.xlsx'

	names = load_data(filename)
	info_dict = get_info_dict(names)
	print(info_dict['LUMA Capital, LLC'])

if __name__ == "__main__":
    main()

	