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


import api

def user_info_traffic_command(bot, update, args):
    if len(args) != 2:
        msg = (
            "Per utilizzare questo comando devi aggiungere id iliad come primo argomento e "
            "password iliad come secondo argomento.\nEsempio:\n\n<code>{} mio_id_iliad "
            "mia_password_iliad</code>"
        )
        msg = msg.format(update.message.text.split(" ")[0])
        update.message.reply_html(msg)
        return

    iliad_id, iliad_password = args
    info = api.get_info(api.login(iliad_id, iliad_password))

    msg = ""
    if info['error'] is False:
        msg += "<b>Le tue soglie e credito iliad:</b>"
        if len(info['ok']) == 0:  # iliad retuned nothing
            msg += "\nNon c'è nulla da mostrare"
        else:
            for i in info['ok']:
                msg += "\n — {}: {}".format(i, info['ok'][i])

    else:  # invalid credentials
        msg += "<b>ERRORE:</b> {}".format(info['error'])

    update.message.reply_html(msg)


def help_command(bot, update):
    msg = (
        "Questo bot permette di conoscere soglie e credito della tua SIM iliad. "
        "Il bot *non è ufficiale* e *non conserva o salva le tue credenziali di accesso*.\n"
        "Il [codice sorgente](https://github.com/91DarioDev/iliadbot) è rilasciato sotto licenza AGPL 3.0.\n\n"
        "*COMANDI SUPPORTATI:*\n\n /info - permette di conoscere stato soglie e credito"
        "\n/help - mostra un messaggio di aiuto"
    )
    update.message.reply_markdown(msg, disable_web_page_preview=True)
