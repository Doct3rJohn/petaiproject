#!/usr/bin/python3
#Author     : Doct3rJohn @_shafiqaiman_

import argparse, netifaces, sys
from netifaces import AF_INET
from func import banner, footer, help_me, shell
from db import the_list
from rich.console import Console; console = Console()

# ID, IP, PORT, SEARCH, LIST, HELP
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-id', '--id', metavar='')
parser.add_argument('-i', '--ip', metavar='')
parser.add_argument('-p', '--port', metavar='')
parser.add_argument('-h', '--help', action="store_true")
parser.add_argument('-l', '--list', action="store_true")
args = parser.parse_args()


if __name__ == "__main__":
    if args.help:
        help_me()
    elif args.list:
        the_list()
    elif args.id or args.ip or args.port:
        try:
            try:
                ip = netifaces.ifaddresses(args.ip)[AF_INET][0]['addr']
            except KeyError:
                console.print("[red][!]Error[/]: Something Wrong!!!")
                sys.exit(1)
            banner()
            shell(args.id, ip, args.port)                
        except TypeError:
            console.print("[light_green][Required][/]: -id/--id[[light_green]ID[/]] -i/--ip[[light_green]IP[/]]  -p/--port[[light_green]PORT[/]]")
    else:
        banner()
        footer()
