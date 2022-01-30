import sys, json, os
from src.budu import help_me, index_err, banner, rvshell
from src.snarai import the_list
from rich.console import Console; console = Console()

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
                        banner()
                        rvshell(shell_id, lhost, lport)
                    else:
                        console.print(f"\n[yellow1 on black]!! '{sys.argv[5]}'[/]\nDo you mean... '[light_green]-p/--lport[/]' <[medium_orchid]listening_port[/]/[medium_orchid]LPORT[/]>")
                else:
                    console.print(f"\n[yellow1 on black]!! '{sys.argv[3]}'[/]\nDo you mean... '[light_green]-i/--lhost[/]' <[medium_orchid]ip_address[/]/[medium_orchid]LHOST[/]>")
            except IndexError:
                print(" Missing an Arguments")
        else:
            print(" Hmmmm It's seems wrong")
    except IndexError:
        banner()
        index_err()