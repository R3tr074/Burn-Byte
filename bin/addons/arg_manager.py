import sys
from bin.addons.banner import *
from bin.addons.menu import menu

red = "\033[38;5;196m"
reset = "\033[0m"


def arg_manager(argv):
    arg_size = len(argv)

    if arg_size == 1:
        main_help()
        return 0

    target = "localhost:1212"
    threads = 3
    time = 10
    method = None
    root = True

    for index, arg in enumerate(argv):
        if arg == "cli":
            target, method, threads, time, root = menu()
            break

        if arg == "--no-root":
            root = False

        if arg in ("-h", "--help", "help"):
            main_help()
            return 0

        if arg in ("-u", "--target"):
            target = argv[index+1]

        if arg in ("-t", "--threads"):
            threads = argv[index+1]
            try:
                if int(threads) < 1 or int(threads) > 200:
                    print(
                        f"{red}[✘] ERROR {threads} not is a valid value to threads flag, use 1 - 200{reset}")
                    return 1
            except:
                print(
                    f"{red}[✘] ERROR {threads} not is a valid value to threads flag, use 1 - 200{reset}")
                return 1
        if arg == "--banner":
            banner()
            return 0

        if arg == "--time":
            time = argv[index+1]
            try:
                if int(time) < 0:
                    print(
                        f"{red}[✘] ERROR {time} not is a valid value to time flag, use any value greater than 0{reset}")
                    return 1
            except:
                print(
                    f"{red}[✘] ERROR {time} not is a valid value to time flag, use any value greater than 0{reset}")
                return 1

        if arg in ("-m", "--method"):
            method = argv[index+1]
            if method in ("help", "--help", "-h", "h"):
                methods_help()
                return 0
            elif method == "E-help":
                reference()
                return 0

    arg = {}
    arg["threads"] = threads
    arg["target"] = target
    arg["time"] = time
    arg["method"] = method
    arg["root"] = root

    return arg
