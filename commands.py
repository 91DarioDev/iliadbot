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
