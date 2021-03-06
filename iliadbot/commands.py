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


import html
from iliadbot import api
from iliadbot import keyboards
from iliadbot import emoji
from iliadbot import utils


def iliad_message_creation(iliad_id, iliad_password, which_dict='info_sim'):
    login = api.login(iliad_id, iliad_password)
    intro = {
        'italia': 'Le tue soglie in Italia {}'.format(emoji.italy),
        'estero': 'Le tue soglie all\'estero {}'.format(emoji.earth),
        'info_sim': 'Info sulla tua sim {}'.format(emoji.info)
    }

    msg = ""
    if login is not None:
        info = api.get_info(login, which_dict)
        msg += "<b>{}: </b>".format(intro[which_dict])
        if len(info) == 0:  # iliad retuned nothing
            msg += "\nNon c'è nulla da mostrare"
        else:
            for i, k in utils.adjust_parsed_info(info).items():
                msg += "\n{}{}: {}".format(emoji.current_choice, html.escape(i), html.escape(k))
        keyboard = keyboards.update_iliad_data_kb(iliad_id, iliad_password, which_dict)
    else:  # invalid credentials
        msg += "<b>ERRORE:</b> {}".format(html.escape("ID utente o password non corretto."))
        keyboard = None
    return msg, keyboard


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
    msg, keyboard = iliad_message_creation(iliad_id, iliad_password)
    update.message.reply_html(msg, reply_markup=keyboard)


def help_command(bot, update):
    msg = (
        "Questo bot permette di conoscere soglie e credito della tua SIM iliad. "
        "Il bot *non è ufficiale* e *non conserva o salva le tue credenziali di accesso*.\n"
        "Il [codice sorgente](https://github.com/91DarioDev/iliadbot) è rilasciato sotto licenza AGPL 3.0.\n\n"
        "*COMANDI SUPPORTATI:*\n\n /info - permette di conoscere stato soglie e credito"
        "\n/help - mostra un messaggio di aiuto"
    )
    update.message.reply_markdown(msg, disable_web_page_preview=True)
