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
                                     
       Check network during page load > any additional files / does it take source from remote addr / pull data / etc
  ''' 

## DIRS

>> test the name of the domain/sub/ other indicator as dir name 

>> e.g. > target.e231.com/e231  - subname.e231.com/subname  


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


>> try open file with editors 

| command | - |
|:---:|:---:|
| vi -filename- |
| vim -filename- |
| emacs -filename- |
| nano -filename-  |
| gedit  (gnome's default editor) |
| leafpad (lxde's default editor) |
| kedit  (KDE's default editor) |
| xdg-open -filename- |
| if viewing doesnt work at all - download to local machine  |

