# FIND EXPLOITS IN THE WILD

>> sometimes vulns and exploits are 1:1 as the lab for example apache + postfix + vulnhub > 
google result shows dedicated write up for this exact match.

# DIRS [WEB]

>> test the name of the domain/sub/ other indicator as dir name 

>> e.g. > target.e231.com/e231 

OR

subname.e231.com/subname  


# SOFTWARE VERSION IDENTIFICATION
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

