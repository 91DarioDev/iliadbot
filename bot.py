import logging

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
    dp.add_handler(CommandHandler('info', commands.user_info_traffic_command, pass_args=True))

    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
