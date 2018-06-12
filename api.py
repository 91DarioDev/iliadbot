import requests
from lxml import html

url = "https://www.iliad.it/account/"

dic = {
	'chiamate_tot' : '//*[@id="page-container"]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/span[1]/text()',
	'gb_tot' : '//*[@id="page-container"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]/span[1]/text()',
	'sms_tot' : '//*[@id="page-container"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/text()',
	'mms_tot' : '//*[@id="page-container"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]/span[1]/text()',
	'consumo_tot' : '//*[@id="page-container"]/div/div[2]/div[2]/div[5]/div[2]/text()',
	'credito_residuo' : '//*[@id="page-container"]/div/div[2]/div[2]/div[5]/div[4]/text()',
}

errors = {
	'credentials': '//*[@id="page-container"]/div/div[1]/div/text()'
}

def login(id, pwd):
	"""
	params: id, pwd
	return: TreeObject
	"""
	data = {"login-ident":id, "login-pwd":pwd}

	r = requests.post(url, data=data)
	tree = html.fromstring(r.content)

	return tree

def get_info(tree):
	"""
	Parse iliad info from tree object of the html profile page
	
	params: TreeObject
	return: dic
	"""
	info = {'ok':{}, 'error':False}

	for err_name, xpath in errors.items():
		error = tree.xpath(xpath)
		if error:
			info['error'] = err_name
			return info

	for k, v in dic.items():
		res = tree.xpath(v)
		info['ok'].update({k:res[0]})

	return info
