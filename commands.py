import api

def user_info_traffic_command(bot, update, args):
    if len(args) != 2:
        print('error')
        return

    iliad_id, iliad_password = args

    info = api.get_info(api.login(iliad_id, iliad_password))

    print(info)
