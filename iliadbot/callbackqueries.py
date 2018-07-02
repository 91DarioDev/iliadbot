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


from iliadbot import commands
from iliadbot import keyboards
from iliadbot import database

from telegram.error import TelegramError


def callback_query(bot, update):
    query = update.callback_query
    database.add_user_db(query.from_user.id)  # update db last activity date

    if query.data.startswith("update_iliad"):
        update_iliad(bot, query)


def update_iliad(bot, query):
    id_iliad = query.data.split(":")[1]
    password_iliad = query.data.split(":")[2]
    try:
        info = query.data.split(":")[3]
    except IndexError:
        info = 'italia'
    msg, keyboard = commands.iliad_message_creation(id_iliad, password_iliad, info)
    try:
        query.edit_message_text(text=msg, reply_markup=keyboard, parse_mode='HTML')
    except TelegramError as e:
        if str(e) != "Message is not modified": print(e)
    query.answer("aggiornato! ✅")
