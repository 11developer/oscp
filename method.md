# most useful directories

• /bin - basic programs (ls, cd, cat, etc.)

• /sbin - system programs (fdisk, mkfs, sysctl, etc)

• /etc - configuration files

• /tmp - temporary files (typically deleted on boot)

• /usr/bin - applications (apt, ncat, nmap, etc.)

• /usr/share - application support and data files 

# Managing Kali Linux Services 

# SSH

commonly used to remotely access a computer 

The SSH service is TCP-based and listens by default on port 22. To start the SSH service in Kali, 

we run systemctl with the start option followed by the service name 

"sudo systemctl start ssh" 

# verify a service running:

by using the ss command and piping the output into grep to search the output for “sshd”: 

command

sudo ss -antlp | grep sshd 

LISTEN 0 128 *:22 *:* users:(("sshd",pid=1343,fd=3)) 
LISTEN 0 128 :::22 :::* users:(("sshd",pid=1343,fd=4)) 

# make a service (SSH) start automatically at boot time

sudo systemctl enable ssh 



# HTTP Service 

apache http service often use for 
 
* providing a platform for downloading files to a victim machine  
* hosting a site 

# start http service 

sudo systemctl start apache2 

# verify http running 

sudo ss -antlp | grep apache 

# start http service at boot time [automatically] 

sudo systemctl enable apache2 


