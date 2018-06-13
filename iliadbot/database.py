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


import sqlite3
import time
import threading

from telegram.ext.dispatcher import run_async


LOCAL = threading.local()
DB_PATH = "database/database.db"

def conn():
    if not hasattr(LOCAL, "db"):
        LOCAL.db = sqlite3.connect(DB_PATH)
    return LOCAL.db


def run_query(query, *params, read=False, one=False):
    connect = conn()
    cursor = connect.cursor()
    try:
        cursor.execute(query, params)
        cursor.connection.commit()
        if read:
            if not one:
                return cursor.fetchall()
            else:
                return cursor.fetchone()
    except:
        cursor.connection.rollback()
        raise
    finally:
        cursor.close()


def create_db():
    query = """
    	CREATE TABLE 
    	IF NOT EXISTS 
    	users (
    		user_id INTEGER PRIMARY KEY, 
    		last_activity TIMESTAMP,
    		registered_at TIMESTAMP
    	)
    """
    run_query(query)


@run_async
def add_user_db(user_id):
    # try to update or ignore
    query = "UPDATE OR IGNORE users SET last_activity = CURRENT_TIMESTAMP WHERE user_id = ?"
    run_query(query, user_id)
    # try to add or ignore
    query = "INSERT OR IGNORE INTO users(user_id, last_activity, registered_at) VALUES (?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
    run_query(query, user_id)

# create the database
create_db()