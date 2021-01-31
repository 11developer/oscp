# DATA TYPES TO LOOK FOR - THINGS OUT OF ORDER / MISCONFIGURED

# Bad permissions. 


Familiarize yourself with which programs are supposed to be SUID, and the unwarranted ones will stand out like a sore thumb. Same thing with write permissions. 

If you can write any root-owned file or folder, it's a huge red flag (or green, for our purposes). Learn your one-liners to find files and directories owned by you,

files and directories owned by root that you can write, and SUID binaries owned by root. I don't generally care about SUID directories, as they're less likely to be a weak point.




# Weird custom software. 


Linux distros often offer an utility to detect executable files that aren't part of an official package. 

That can help you find that odd program that was put there for you to exploit.



# Internal listening services. 


If your "netstat -antp" shows listening services that only accept 127.0.0.1 or are otherwise filtered by iptables, 

immediately tunnel them out via SSH and poke at them from your kali box. They're often there for a reason.



# Arguments on running root processes. 

This is something that I found most priv check scripts to be deficient at. 

Just "ps aux |grep root" (grep here often helps deal with cropped terminals) and check the command line arguments of each running root-owned service. 

Sometimes you spot weird stuff, like relative paths. Speaking of weird root processes...



# Processes running as root that don't have any business doing that. 

Mysql is a big offender here; if it's running as root you probably want to have a go at it. 

Services that don't really sound like they need to have full administrative control of the system probably shouldn't.



# Known bad packages with SUID executables.

While reading through the list of SUID binaries, it's worth looking at their package version (privchecker will get that for you) 

and making sure they aren't vulnerable to privesc exploits. Exim is a good example of this.



# Strangeness in the common "sensitive" files. 

Know the permissions of /etc/passwd, /etc/shadow, /etc/cron* by heart, as well as the common service config files, 

and be ready to spot when you can read or write something you shouldn't. Also, if you got in with credentials, always check what sudo permissions you have. 

You can be pleasantly surprised.



ref 

https://www.reddit.com/r/oscp/comments/9ystub/i_absolutely_suck_at_privilege_escalation/ 


always worth taking a very close look at everything you find on your user's home directory. 

If you find config files, scripts, binaries, text files.... It is extremely likely they're related to the path you need to take. 
