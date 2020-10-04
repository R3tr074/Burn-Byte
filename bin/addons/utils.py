import ctypes
import os


def root_privileges():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def __path(*args):
    complete_path = args[0]
    if os.name == "nt":
        join = "\\"
    else:
        join = "/"

    for path in args:
        if args[0] == path:
            continue
        complete_path = complete_path+join+path
    return complete_path
