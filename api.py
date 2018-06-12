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
	info = {}
	for k, v in dic.items():
		info.update({k:tree.xpath(v)[0]})
	return info
	
