import sys, json, os
from src.budu import help_me, index_err, banner
from src.budu import c
from src.crab import the_list

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
                os.system(f"nc -lnvp {lhost} {lport}")
                break

def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h": 
            help_me()
        elif sys.argv[1] == "--list":
            the_list()
        elif sys.argv[1] == "--shell" or sys.argv[1] == "-s": 
            try:
                shell_id = sys.argv[2]
                if sys.argv[3] == "--lhost" or sys.argv[3] == "-lh":
                    lhost = sys.argv[4]
                    if sys.argv[5] == "--lport" or sys.argv[5] == "-lp":
                        lport = sys.argv[6]
                        rvshell(shell_id, lhost, lport)
                    else:
                        print(f"\n {c.BRED}#  '{sys.argv[5]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-lp/--lport'{c.RESET} <{c.BBLUE}listening_port{c.RESET}/{c.BBLUE}LPORT{c.RESET}>")
                else:
                    print(f"\n {c.BRED}#  '{sys.argv[3]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-lh/--lhost'{c.RESET} <{c.BBLUE}ip_address{c.RESET}/{c.BBLUE}LHOST{c.RESET}>")
            except IndexError:
                print(" Missing an Arguments")
        else:
            print(" Hmmmm It's seems wrong")
    except IndexError:
        banner()
        index_err()