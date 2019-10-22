import glovar as GlobalVar


def get():
    print(('id GlobalVar: ', id(GlobalVar)))
    print(("------get mq_client in get.py------mq_client: " + str(GlobalVar.get_mq_client())))
