# Import modules
import os
import sys
import platform
from time import ctime
from rich.console import Console

# Define styled print
print = Console().print

purple = "blue_violet"
yellow = "yellow1"
red = "red3"

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
    [{red}]:=== Critical error:"[/{red}]
    [{purple}]MESSAGE: {message}[/{purple}]
    [{purple}]ERROR: {error}[/{purple}]
    [{red}]:=== Python info:"[/{red}]
    [{purple}]PYTHON VERSION: {py_version}[/{purple}]
    [{purple}]PYTHON BUILD: {py_build}[/{purple}]
    [{purple}]PYTHON COMPILER: {py_compiler}[/{purple}]
    [{purple}]SCRIPT LOCATION: {script_location}[/{purple}]
    [{purple}]CURRENT LOCATION: {current_location}[/{purple}]
    [{red}]:=== System info:"[/{red}]
    [{purple}]SYSTEM: {system}[/{purple}]
    [{purple}]RELEASE: {system_realese}[/{purple}]
    [{purple}]VERSION: {system_version}[/{purple}]
    [{purple}]ARCHITECTURE: {system_architecture}[/{purple}]
    [{purple}]PROCESSOR: {system_processor}[/{purple}]
    [{purple}]MACHINE: {system_machine}[/{purple}]
    [{purple}]NODE: {system_node}[/{purple}]
    [{purple}]TIME: {system_time}[/{purple}]
    [{red}]:=== Report:"[/{red}]
    [{yellow}]Please report it here: https://github.com/R3tr074/BurnByte/issues/new"[/{yellow}]
    """
    )
    sys.exit(5)
