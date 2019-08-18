# WEB
# ports & services recon
~~~
TCP SCAN 
nmap -sC -sV -oA -ip-
Nmap -Pn -p- -vv -ip-
UDP SCAN
Nmap -Pn -p- -sU -vv -ip-

Other: All scan nmap -A -Pn IP -vv 
~~~
# Nmap targeted vuln scan
~~~
https://nmap.org/nsedoc/ 
example of script usage:
nmap --script=VULN-TEST-XYZ -p 3366 <targets>
Grab banners manually for more clarity: nc -nv <ip-address> <port>
 ~~~ 
# semi automatic scanners (recon + vuln assesement + exploitation)
1. Kaboom https://github.com/Leviathan36/kaboom 
info gather: nmap +  dirb 
vuln assesment: Nikto - Dirb | Nmap - Metasploit | Searchsploit - Metasploit 
BF:hydra 

2. Vanquish https://github.com/frizb/Vanquish 


# Subdomains check 
~~~
bruteforce: 
knock # python knockpy.py target.com
records: 
sublist3r # python3 sublist3r.py -v -d target.com
OWASP:
https://github.com/OWASP/Amass/ 

Any hidden subdomains? 
*.*.domain.xyz
~~~
# Any web dirs/sensitive data on subdomains 
~~~
# Usually sub domains are less secure / more misconfigurations 
Nikto -port {web ports} -host ip address -o output file.txt

Dirb http{s}://ip address:port /usr/share/wordlist/dirb/{common/small/big/targeted}.txt
or
Gobuster -u http://<ip-address> -w /usr/share/Seclists/Discovery/Web_Content/common.txt

# recomended to scan IP instead of domain name

also /usr/share/secLists/Discovery folder has some great word lists
If no dirs visible try /big.txt
if no dirs/contect found - test for customized dirs based on target name, clues from pages- etc.

Use burpsuite - catch request / response data from headers etc. 

Do you see any interesting directory containing sensitive data?
~~~
# Are there any exploits available publicly from the services discovered from nmap scan?
~~~
Searchsploit <service name> 
Or general search globally maybe https://sploitus.com/ for different sources
~~~
# Manual web testing 
~~~
Check the Page Source, Inspect elements, view cookies, tamper data, use curl/wget

    Any info exposure 
- hardcoded crednetials or potential leads revealed to client side 
    Any version info?
- from responce headers/ source code / fingerprinting app 
    Headers 
- allowes methods  ? server type / other data 
    Dirs or syntax crawlers cannot catch?
manually go to robots.txt or sitemap.xml if exist 
- does the source code reveal links or redirect points to other content on the server  hidden ?
    
    curl -v -X OPTIONS http://<targetip>/test/
~~~

# Search online (e.g. GitHub) if the application used is open source: this may assist in site enumeration and guessing versions/dirs/paths/etc.!

# part of step5 > Check HTTP Options (PUT - file upload..etc)

# Check for Input Validation in forms 
~~~
(like: 1′ or 1=1 limit 1;#   AND   1′ or 1=1–)
    NULL or null
        Possible error messages returned.
    ‘ , ” , ; , <!
        Breaks an SQL string or query; used for SQL, XPath and XML Injection tests.
    – , = , + , ”
        Used to craft SQL Injection queries.
    ‘ , &, ! , ¦ , < , >
        Used to find command execution vulnerabilities.
    ../
        Directory Traversal Vulnerabilities. 
                                     
       Check network during page load > any additional files / does it take source from remote addr / pull data / etc
~~~                                   
# NETWORK
                                     
# Semi auto recon + exploit suggest based on results - https://github.com/frizb/Vanquish                                      
# Are there any NETBIOS, SMB, RPC ports discovered from Step 1?

# SMB

Port 139 and 445- SMB/Samba shares
Samba is a service that enables the user to share files with other machines
works the same as a command line FTP client, may browse files without even having credentials

# Share List:
smbclient --list <targetip>
smbclient -L <targetip>

# Check SMB vulnerabilities:
nmap --script=smb-check-vulns.nse <targetIP> -p445

# basic nmap scripts to enumerate shares and OS discovery
nmap -p 139,445 <targetIP> --script smb-enum-shares.nse smb-os-discovery.nse

# Connect using Username
smbclient -L <targetip> -U username -p 445

# Connect to Shares
smbclient \\\\<targetip>\\ShareName
smbclient \\\\<targetip>\\ShareName -U john

# enumarete with smb-shares, -a “do everything” option
enum4linux -a 192.168.1.14

# learn the machine name and then enumerate with smbclient
nmblookup -A 192.168.1.14
smbclient -L <server_name> -I 192.168.1.14

# rpcclient - Connect with a null-session (only works for older windows servers)
rpcclient -U james 10.10.10.52
rpcclient -U "" 192.168.1.105
(press enter if asks for a password)
rpcclient $> srvinfo
rpcclient $> enumdomusers
rpcclient $> enumalsgroups domain
rpcclient $> lookupnames administrators
rpcclient> querydominfo
rpcclient> enumdomusers
rpcclient> queryuser john

# scan for vulnerabilities with nmap for 139,445
nmap --script "vuln" <targetip> -p139,445

# SMTP
# telnet or netcat connection
nc <targetip> 25
VRFY root
# Check for commands
nmap -script smtp-commands.nse <targetip>


# Port 111 - RPC

Rpcbind can help us look for NFS-shares. So look out for nfs. Obtain list of services running with RPC:

rpcbind -p <targetip>
rpcinfo –p x.x.x.x

using nmap, see which port NFS is listening
locate *rpc*.nse
nmap --script rpcinfo.nse <targetip> -p 111

-------------------------

# NFS

# to find the public share
locate *nfs*.nse
nmap --script nfs-showmount.nse <targetip>

# mount the share to a folder under /tmp
mkdir /tmp/nfs
/sbin/mount.nfs <targetip>:/home/box /tmp/nfs
~~~
enum4linux -a <ip address>
~~~
~~~
Rpcclient <ip address> -U -N
~~~
~~~
Rpcinfo: What services are running? Rpcinfo -p <target ip>
~~~
~~~
Is portmapper running? Is rlogin running? Or NFS or Mountd?

http://etutorials.org/Networking/network+security+assessment/Chapter+12.+Assessing+Unix+RPC+Services/12.2+RPC+Service+Vulnerabilities/

Showmount -e <ip address>/<port>

Can you mount the smb share locally?

Mount -t cifs //<server ip>/<share> <local dir> -o username=”guest”,password=””

Rlogin <ip-address>

Smbclient -L \\<ip-address> -U “” -N

Nbtscan -r <ip address>

Net use \\<ip-address>\$Share “” /u:””

Net view \\<ip-address>

Check NMAP Scripts for SMB, DCERPC and NETBIOS

# Any SMTP ports available?

Enumerate Users:

Mail Server Testing

    Enumerate users
        VRFY username (verifies if username exists – enumeration of accounts)
        EXPN username (verifies if username is valid – enumeration of accounts)

# SNMP ports?
~~~
~~~
Default Community Names: public, private, cisco, manager

Enumerate MIB:

System Processes
Running Programs
Processes Path
Storage Units
Software Name
User Accounts
TCP Local Ports

Tools:
Onesixtyone – c <community list file> -I <ip-address>
Snmpwalk -c <community string> -v<version> <ip address>
Eg: enumerating running processes:
snmpwalk -c public -v1 192.168.11.204 1.3.6.1.2.1.25.4.2.1.2
~~~

# FTP Ports ?
~~~
Is anonymous login allowed?

If yes, is directory listing possible? Can a file be ‘get’ or ‘send’?

Use browser: ftp://<ip-address> , What do you find?
~~~

# Password Cracking / Brute Forcing
~~~

Try this as the last resort or in case the Passwd/Shadow/SAM files are in possession:

For linux, first combine passwd & shadow files:  unshadow [passwd-file] [shadow-file] > unshadowed.txt

Then, use John on the unshadowed file using a wordlist or rules mangling : 
john –rules –wordlist=<wordlist file> unshadowed.txt

Identifying Hash: hash-identifier

For other services, use Medusa or Hydra. Eg:

Hydra -L <username file> -P <Password file> -v <ip-address> ssh

Medusa -h <ip-address> -U <username file> -P <password file> -M http -m DIR:/admin -T 30

Using hashcat for cracking hashes:

For WordPress MD5 with salt: hashcat -m 400 -a 0 <hash file> <wordlist file>

Sample Password list: /usr/share/wordlist/rockyou.txt
~~~

# Step 11: Packet Sniffing
~~~

Use Wireshark / tcpdump to capture traffic on the target host:

“tcpdump -i tap0 host <target-ip> tcp port 80 and not arp and not icmp -vv”
~~~


# References 
https://paper.dropbox.com/doc/OSCP-Methodology-EnVX7VSiNGZ2K2QxCZD7Q  

