import sys, json
from budu import help_me, index_err, banner, c, the_list

def rvshell(id, lhost, lport):
    with open("yummy.json", 'r') as f:
        data = json.loads(f.read())
        for i in data["reverse_shell_list"]:
            if i['id'] == id:
                payload = i['object']
                xp = payload.replace("lhost", lhost)
                print(xp.replace("lport", lport))
                break

def main():
    try:
        if sys.argv[1] == "--help":
            help_me()
        elif sys.argv[1] == "--list":
            the_list()
        elif sys.argv[1] == "-r":
            try:
                revshell = sys.argv[2]
                if sys.argv[3] == "-i":
                    lhost = sys.argv[4]
                    if sys.argv[5] == "-p":
                        lport = sys.argv[6]
                        rvshell(revshell, lhost, lport)
                    else:
                        print(f"\n {c.BRED}#  '{sys.argv[5]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-p'{c.RESET} <{c.BBLUE}listening_port{c.RESET}/{c.BBLUE}LPORT{c.RESET}>")
                else:
                    print(f"\n {c.BRED}#  '{sys.argv[3]}'  {c.RESET} \n Do you mean... {c.BGREEN}'-i'{c.RESET} <{c.BBLUE}ip_address{c.RESET}/{c.BBLUE}LHOST{c.RESET}>")
            except IndexError:
                print(" Missing an Arguments")
        else:
            print(" Hmmmm It's seems wrong")
    except IndexError:
        banner()
        index_err()