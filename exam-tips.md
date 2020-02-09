# exploitation
> sometimes these are 1:1 as the lab practice for example apache + postfix + vulnhub > 
google result shows dedicated write up for this exact match.


# dirs
| Name | Source | 
|:---:|:---:|
|test the name of the domain/sub/ other indicator as dir name |
|e.g. > target.e231.com/e231 or  subname.e231.com/subname  |

# identifying versions 
| Name | Source | 
|:---:|:---:|
| scanner output |
| headers |
| bottom page  |
| mouseoverview may reveal different version on object in web  |
| source code [if not direct reveal, then based on libraries, other indicators] |
| connect to services attempt [-sC] |
| banner grabbing [nc] |
| fingerprint app [scan] |


# viewing flag.txt 
| Name | Source | 
|:---:|:---:|
|view OR dl|
| cat | OR | cat -A |
| head -filename- |
| less -filename-  |
| tail -f -filename- |
| more -filename- |

type -filename-

>> try open file with editors 

| Name | Source | 
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

