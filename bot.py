# iliadbot - A telegram bot for telegram public groups leaderboards
# Copyright (C) 2018  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)
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


import logging

import commands
import config

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    print("\nrunning...")
    # define the updater
    updater = Updater(token=config.BOT_TOKEN)
    
    # define the dispatcher
    dp = updater.dispatcher

    # define jobs
    j = updater.job_queue

    # commands
    dp.add_handler(CommandHandler(('start, help'), commands.help_command))
    dp.add_handler(CommandHandler('info', commands.user_info_traffic_command, pass_args=True))

    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
