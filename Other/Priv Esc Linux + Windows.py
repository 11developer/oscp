Linux/win priv-esc / shell escape
USE THIS also FOR PRIV-ESC https://paper.dropbox.com/doc/OSCP-Methodology-EnVX7VSiNGZ2K2QxCZD7Q 

# Test commands allowed / characters to determine what shell you're in and how its configured - and escape accordingly 

# MANUAL TESTS ON TARGET MACHINE (LINUX)
    https://fireshellsecurity.team/restricted-linux-shell-escaping-techniques/
    https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
    add here spec pdf


# RUN ON LINUX TARGET 

https://github.com/codingo/OSCP-2/blob/master/BASH/CronJobChecker.sh
Cron job checker script that may reveal root cron jobs by checking for newly spawned processes

https://github.com/rebootuser/LinEnum
or
http://pentestmonkey.net/tools/audit/unix-privesc-check
or
https://www.darknet.org.uk/2015/06/unix-privesc-check-unixlinux-user-privilege-escalation-scanner/
Scripted Local Linux Enumeration & Privilege Escalation Checks 

https://github.com/PenturaLabs/Linux_Exploit_Suggester
or
https://github.com/mzet-/linux-exploit-suggester
Linux Exploit Suggester; based on operating system release number 

    
    
# WINDOWS TESTS

https://github.com/codingo/OSCP-2/blob/master/Windows/WinPrivCheck.bat
Comprehensive Windows privesc script that checks KBs as well as common misconfigurations
        
https://github.com/foxglovesec/RottenPotato
Local Privilege Escalation from Windows Service Accounts to SYSTEM

https://github.com/PowerShellMafia/PowerSploit
PowerSploit - A PowerShell Post-Exploitation Framework

#Other nice write-ups for windows priv-esc 
https://toshellandback.com/2015/11/24/ms-priv-esc/
https://pentest.blog/windows-privilege-escalation-methods-for-pentesters/
    
