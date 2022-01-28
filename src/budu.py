import sys, json

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
    print(" \▓▓      \▓▓▓▓▓▓▓▓   \▓▓   \▓▓   \▓▓\▓▓▓▓▓▓ v0.0.3\n")                                                                                        
                                            
def help_me():
    print("")
    print(f" {c.BBLUE}###################################################")
    print(f" #                                                 #{c.RESET}")
    print(f" {c.BBLUE}#{c.RESET} {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -s 1 -lh 10.10.10.10 -lp 1000{c.RESET} {c.BBLUE}#{c.RESET}")
    print(f" {c.BBLUE}#                                                 #")
    print(f" ###################################################{c.RESET}\n")
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-s [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-lh [{c.BGREEN}LHOST{c.RESET}]]  [-lp [{c.BGREEN}LPORT{c.RESET}]]")
    print(f" \n\n {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}OPTIONS:{c.RESET}")
    print(" -s   / --shell <reverse_shell_id>     :   Reverse Shell ID")
    print(" -lh  / --lhost <ip_address>/LHOST     :   Ip Address")
    print(" -lp  / --lport <listening_port/LPORT> :   Port")
    print(" ")
    print(f" {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}WHY NOT OPTIONS:{c.RESET}")
    print(" --help:      show help")
    print(" --list:      list all reverse shell [ID]")

def index_err():
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-s [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-lh [{c.BGREEN}LHOST{c.RESET}]]  [-lp [{c.BGREEN}LPORT{c.RESET}]]\n\n")
    print(f" {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -s 1 -lh 10.10.10.10 -lp 1000{c.RESET}")
    print(f" {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py --shell 1 --lhost 10.10.10.10 --lport 1000{c.RESET}")
    print(f" {c.BYELLOW}Error{c.RESET}: Sorry, Try This '{c.BGREEN}--help{c.RESET}'")
