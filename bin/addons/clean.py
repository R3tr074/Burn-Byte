# Import modules
import os

# Clear command line
def clear():
    if os.name == "nt":
        os.system("@cls & @title Burn Byte & @color e")
    else:
        os.system("clear")
