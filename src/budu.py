import sys, json, os

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
    print(f" {c.BBLUE}#{c.RESET} {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -id 1 -i 10.10.10.10 -p 1000{c.RESET} {c.BBLUE}#{c.RESET}")
    print(f" {c.BBLUE}#                                                 #")
    print(f" ###################################################{c.RESET}\n")
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-id [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-i [{c.BGREEN}LHOST{c.RESET}]]  [-p [{c.BGREEN}LPORT{c.RESET}]]")
    print(f" \n\n {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}OPTIONS:{c.RESET}")
    print(" -id / --id <reverse_shell_id>        :   Reverse Shell ID")
    print(" -i  / --lhost <ip_address>/LHOST     :   Ip Address")
    print(" -p  / --lport <listening_port/LPORT> :   Port")
    print(" ")
    print(f" {c.UNDERLINE}{c.BOLD}{c.BBLACK}{c.BYELLOW}WHY NOT OPTIONS:{c.RESET}")
    print(" --help:      show help")
    print(" --list:      list all reverse shell [ID]")

def index_err():
    print(f" {c.BGREEN}{c.UNDERLINE}Usage:{c.RESET} petai.py [{c.BGREEN}--help{c.RESET}]  [-id [{c.BGREEN}REVERSE SHELL ID{c.RESET}]]  [-i [{c.BGREEN}LHOST{c.RESET}]]  [-p [{c.BGREEN}LPORT{c.RESET}]]\n\n")
    print(f" {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py -id 1 -i 10.10.10.10 -p 1000{c.RESET}")
    print(f" {c.BOLD}{c.BBLACK}{c.BYELLOW}Example: petai.py --id 1 --lhost 10.10.10.10 --lport 1000{c.RESET}")
    print(f" {c.BYELLOW}Error{c.RESET}: Sorry, Try This '{c.BGREEN}--help{c.RESET}'")

def rvshell(id, lhost, lport):
    with open("src/jering.json", 'r') as f:
        data = json.loads(f.read())
        for i in data["reverse_shell_list"]:
            if i['id'] == id:
                payload = i['shell']
                xp = payload.replace("lhost", lhost)
                vista = xp.replace("lport", lport)
                print(f"\n {c.BOLD}{c.BGREEN}The Command:{c.RESET} {vista}")
                print("---------------------------------------------------")
                print(f" [{c.BGREEN}X{c.RESET}] {c.BYELLOW}stARt LIsTeNing...{c.RESET}")
                os.system(f"nc -lnvp {lport}")
                break