import sys, json, os
from src.budu import help_me, index_err, banner, rvshell, c
from src.snarai import the_list

def main():
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h": 
            help_me()
        elif sys.argv[1] == "--list":
            the_list()
        elif sys.argv[1] == "--id" or sys.argv[1] == "-id": 
            try:
                shell_id = sys.argv[2]
                if sys.argv[3] == "--lhost" or sys.argv[3] == "-i":
                    lhost = sys.argv[4]
                    if sys.argv[5] == "--lport" or sys.argv[5] == "-p":
                        lport = sys.argv[6]
                        rvshell(shell_id, lhost, lport)
                    else:
                        print(f"\n {c.BRED}#  '{sys.argv[5]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-p/--lport'{c.RESET} <{c.BBLUE}listening_port{c.RESET}/{c.BBLUE}LPORT{c.RESET}>")
                else:
                    print(f"\n {c.BRED}#  '{sys.argv[3]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-i/--lhost'{c.RESET} <{c.BBLUE}ip_address{c.RESET}/{c.BBLUE}LHOST{c.RESET}>")
            except IndexError:
                print(" Missing an Arguments")
        else:
            print(" Hmmmm It's seems wrong")
    except IndexError:
        banner()
        index_err()