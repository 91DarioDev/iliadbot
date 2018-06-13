import api

def user_info_traffic_command(bot, update, args):
    if len(args) != 2:
        print('error')
        return

    iliad_id, iliad_password = args
    info = api.get_info(api.login(iliad_id, iliad_password))

    msg = ""
    if info['error'] is False:
        msg += "Le tue soglie e credito iliad:"
        for i in info['ok']:
            msg += "\n{}: {}".format(i, info['ok'][i])

    else:  # invalid credentials
        msg += "<b>ERRORE:</b> {}".format(info['error'])

    print(msg)
