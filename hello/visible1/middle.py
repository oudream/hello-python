import glovar as GlobalVar


def middle():
    print(('id GlobalVar: ', id(GlobalVar)))
    print(("------middle mq_client in middle.py------mq_client: " + str(GlobalVar.get_mq_client())))
