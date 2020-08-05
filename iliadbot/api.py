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

# italia xpaths
def get_italia(tree):
    dic_italia = collections.OrderedDict()
    dic_italia["{} chiamate".format(emoji.telephone)] = tree.xpath('/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/span[1]/text()')[0]
    dic_italia["{} sms".format(emoji.sms)] = tree.xpath('/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div/div[1]/span[1]/text()')[1]
    dic_italia["{} internet".format(emoji.internet)] = tree.xpath('/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[1]/text()')[2]
    dic_italia["{} mms".format(emoji.mms)] =tree.xpath('/html/body/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[1]/span[1]/text()')[3]
    return dic_italia

# estero xpaths
def get_estero(tree):
    dic_estero = collections.OrderedDict()
    dic_estero["{} chiamate".format(emoji.telephone)] = tree.xpath('//div[@class="conso-infos conso-roaming"]//div[@class="conso__text"]/span[2]/text()')[0]
    dic_estero["{} sms".format(emoji.sms)] = tree.xpath('//div[@class="conso-infos conso-roaming"]//div[@class="conso__text"]/span[2]/text()')[1]
    dic_estero["{} internet".format(emoji.internet)] = tree.xpath('//div[@class="conso-infos conso-roaming"]//div[@class="conso__text"]/span[2]/text()')[2]
    dic_estero["{} mms".format(emoji.mms)] =tree.xpath('//div[@class="conso-infos conso-roaming"]//div[@class="conso__text"]/span[2]/text()')[3]
    return dic_estero

def get_general(tree):
    dic_general_info = collections.OrderedDict()
    dic_general_info["{} utente".format(emoji.user)] =  tree.xpath('//div[@class="current-user__infos"]/div[1]/text()')[0]
    dic_general_info["{} id utente".format(emoji.user)] = tree.xpath('//div[@class="current-user__infos"]/div[2]/text()')[0]
    dic_general_info["{} numero".format(emoji.user)] = tree.xpath('//div[@class="current-user__infos"]/div[3]/text()')[0]
    #dic_general_info["{} consumo totale".format(emoji.money)] = "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[6]/div[2]"   #removed from website
    dic_general_info["{} credito".format(emoji.money)] = tree.xpath('//div[@class="page p-conso"]/h2/b/text()')[0]
    dic_general_info["{} rinnovo".format(emoji.renewal)] = tree.xpath('//div[@class="end_offerta"]/text()')[0].replace("\n", "").replace("    ", "")
    return dic_general_info

def login(id, pwd):
    """
    params: id, pwd
    return: TreeObject
    """
    data = {"login-ident":id, "login-pwd":pwd}

    r = requests.post(url, data=data)
    tree = html.fromstring(r.content)

    error = tree.xpath('//div[@class="flash flash-error"]/text()')

    # Return False if wrong credentials
    if error:
        return None

    return tree

def get_info(tree, which_dic):
    """
    Parse iliad info from tree object of the html profile page
    
    params: TreeObject
    return: dic
    """

    # which_dic to take
    if which_dic == 'italia':
        dic = get_italia(tree)
    elif which_dic == 'estero':
        dic = get_estero(tree)
    else:
        dic = get_general(tree)

    return dic
