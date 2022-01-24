import sys

class c:
    BMAGENTA = '\033[95m'
    BBLACK = '\033[100m'
    BBLUE = '\033[94m'
    BCYAN = '\033[96m'
    BGREEN = '\033[92m'
    BYELLOW = '\033[93m'
    BRED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
    print(" _______  ________ ________  ______  ______ ")
    print("|       \|        \        \/      \|      \\")
    print("| ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓\\\▓▓▓▓▓▓")
    print("| ▓▓__/ ▓▓ ▓▓__      | ▓▓  | ▓▓__| ▓▓ | ▓▓  ")
    print("| ▓▓    ▓▓ ▓▓  \     | ▓▓  | ▓▓    ▓▓ | ▓▓  ")
    print("| ▓▓▓▓▓▓▓| ▓▓▓▓▓     | ▓▓  | ▓▓▓▓▓▓▓▓ | ▓▓  ")
    print("| ▓▓     | ▓▓_____   | ▓▓  | ▓▓  | ▓▓_| ▓▓_ ")
    print("| ▓▓     | ▓▓     \  | ▓▓  | ▓▓  | ▓▓   ▓▓ \\")
    print(" \▓▓      \▓▓▓▓▓▓▓▓   \▓▓   \▓▓   \▓▓\▓▓▓▓▓▓ v0.0.2\n")                                                                                        
                                            
def help_me():
    print("")
    print(f" {c.BBLUE}#################################################")
    print(f" #                                               #{c.RESET}")
    print(f" {c.BBLUE}#{c.RESET} {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -r 1 -i 10.10.10.10 -p 1000{c.RESET} {c.BBLUE}#{c.RESET}")
    print(f" {c.BBLUE}#                                               #")
    print(f" #################################################{c.RESET}\n")
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-r [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-i [{c.BGREEN}LHOST{c.RESET}]]  [-p [{c.BGREEN}LPORT{c.RESET}]]")
    print(f" \n\n {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}OPTIONS:{c.RESET}")
    print(" -r  <reverse_shell_id>     :   Reverse Shell ID")
    print(" -i  <ip_address>/LHOST     :   Ip Address")
    print(" -p  <listening_port/LPORT> :   Port")
    print(" ")
    print(f" {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}WHY NOT OPTIONS:{c.RESET}")
    print(" --help:      show help")
    print(" --list:      list all reverse shell [ID]")

def index_err():
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-r [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-i [{c.BGREEN}LHOST{c.RESET}]]  [-p [{c.BGREEN}LPORT{c.RESET}]]\n\n")
    print(f" {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -r 1 -i 10.10.10.10 -p 1000{c.RESET}")
    print(f" {c.BYELLOW}Error{c.RESET}: Sorry, Try This '{c.BGREEN}--help{c.RESET}'")

def the_list():
    print("")
    print("- [Reverse Shell Type] -")
    print("_____________________________________")
    print("|ID   |       Reverse Shell          |")
    print("|=====+==============================+")
    print("| 1   |      bash -i TCP             |")
    print("| 2   |      bash -i UDP             |")
    print("| 3   |      nc -c                   |")
    print("| 4   |      nc -e                   |")
    print("| 5   |      nc mkfifo               |")
    print("| 6   |      perl                    |")
    print("| 7   |      python3                 |")
    print("| 8   |      php exec                |")
    print("| 9   |      php shell exec          |")
    print("| 10  |      php `                   |")
    print("| 11  |      php system              |")
    print("| 12  |      php passthru            |")
    print("| 13  |      php popen               |")
    print("| 14  |      ruby                    |")
    print("+-----+------------------------------+")