# OSCP forum - https://forums.offensive-security.com/ 

# FIND VULN POC's IN THE WILD

>> sometimes vulns and exploits are 1:1 as the lab for example apache + postfix + vulnhub > 
google result shows dedicated write up for this exact match.

## TARGETED NMAP SCAN (nse) 

https://nmap.org/nsedoc/ 
example of script usage:
nmap --script=VULN-TEST-XYZ -p 3366 <targets>
Grab banners manually for more clarity: nc -nv <192.168.x.x> <port>


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