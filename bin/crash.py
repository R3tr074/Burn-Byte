# Import modules
import os
import sys
import platform
from time import ctime
from stringcolor import *

purple = "#6502dd"
red = "#ff0033"
yellow = "#ffcc00"

""" This function will stop the program when a critical error occurs """

py_version = platform.python_version()
py_build = "{}, DATE: {}".format(*platform.python_build())
py_compiler = platform.python_compiler()
script_location = os.path.dirname(os.path.realpath(sys.argv[0]))
current_location = os.getcwd()

system = platform.system()
system_realese = platform.release()
system_version = platform.version()
system_architecture = {"{} {}".format(*platform.architecture())}
system_processor = platform.processor()
system_machine = platform.machine()
system_node = platform.node()
system_time = ctime()


def CriticalError(message, error):
    print(
        f"""
    {cs(":=== Critical error:", red)}
    {cs(f"MESSAGE: {message}", purple)}
    {cs(f"ERROR: {error}", purple)}
    {cs(":=== Python info:", red)}
    {cs(f"PYTHON VERSION: {py_version}", purple)}
    {cs(f"PYTHON BUILD: {py_build}", purple)}
    {cs(f"PYTHON COMPILER: {py_compiler}", purple)}
    {cs(f"SCRIPT LOCATION: {script_location}", purple)}
    {cs(f"CURRENT LOCATION: {current_location}", purple)}
    {cs(":=== System info:", red)}
    {cs(f"SYSTEM: {system}", purple)}
    {cs(f"RELEASE: {system_realese}", purple)}
    {cs(f"VERSION: {system_version}", purple)}
    {cs(f"ARCHITECTURE: {system_architecture}", purple)}
    {cs(f"PROCESSOR: {system_processor}", purple)}
    {cs(f"MACHINE: {system_machine}", purple)}
    {cs(f"NODE: {system_node}", purple)}
    {cs(f"TIME: {system_time}", purple)}
    {cs(":=== Report:", red)}
    {cs("Please report it here: https://github.com/R3tr074/BurnByte/issues/new", yellow)}
    """
    )
    sys.exit(5)
