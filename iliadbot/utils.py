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
	new = {}

	for i, k in dic.items():
		#print(k)

		if i == "{} numero".format(emoji.user):
			k = k.split(": ")[1]

		elif i == "{} id utente".format(emoji.user):
			k = k.split(": ")[1]

		elif i == "{} rinnovo".format(emoji.renewal):
			k = k.split("alle ")[1]

		new.update({i:k})
	return new
