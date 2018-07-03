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


from iliadbot import emoji

def adjust_parsed_info(dic):
    for i in dic:

        if i[0] == "{} numero".format(emoji.user):
            i[1] = i[1].split(": ")[1]

        elif i[0] == "{} id utente".format(emoji.user):
            i[1] = i[1].split(": ")[1]

        elif i[0] == "{} rinnovo".format(emoji.renewal):
            i[1] = i[1].split("alle ")[1]

        elif i[0] == "{} chiamate".format(emoji.telephone):
            i[1] = " ".join(i[1].split(": ")[1:])  # remove double "chiamate"
    
    return dic
