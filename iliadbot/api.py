# iliadbot - A telegram bot to check your iliad's balance and quotas
# Copyright (C) 2018  iliadbot authors: see AUTHORS file at the top-level directory of this repo
#
# iliadbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iliadbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with iliadbot.  If not, see <http://www.gnu.org/licenses/>.


import requests
from lxml import html
import re
import collections
from iliadbot import emoji


url = "https://www.iliad.it/account/"

dic = collections.OrderedDict()
dic["{} chiamate".format(emoji.telephone)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]"
dic["{} sms".format(emoji.sms)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]"
dic["{} internet".format(emoji.internet)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[1]"
dic["{} mms".format(emoji.mms)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div[1]"
dic["{} consumo totale".format(emoji.money)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[5]/div[2]"
dic["{} credito residuo".format(emoji.money)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[5]/div[4]"

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
    info = {'ok':[], 'error':False}

    for err_name, xpath in errors.items():
        error = tree.xpath(xpath)
        if error:
            info['error'] = err_name
            return info

    for k, v in dic.items():
        res = tree.xpath(v)
        if res:
            res_child_text = res[0].text_content()
            res_child_text_no_spaces = re.sub(' +',' ', res_child_text)
            info['ok'].append([k, res_child_text_no_spaces])
    return info
