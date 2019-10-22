import glovar as GlobalVar


def set():
    print(('id GlobalVar: ', id(GlobalVar)))
    GlobalVar.set_mq_client(10)
    print(("------set mq_client in set.py------mq_client: " + str(GlobalVar.get_mq_client())))
