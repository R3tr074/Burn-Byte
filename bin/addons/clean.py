import os


def clear():
    """
    Clear command line in multiplataform
    """
    if os.name == "nt":
        os.system("@cls & @title Burn Byte & @color e")
    else:
        os.system("clear")
