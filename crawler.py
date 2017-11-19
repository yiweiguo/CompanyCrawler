from openpyxl import load_workbook

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





filename = 'Financial_company _UNlist.xlsx'

names = load_data(filename)
for name in names:
	print(name)