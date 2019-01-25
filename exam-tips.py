If you're stuck in the lab/exam unable to run exloit, find vuln.. etc. 
Look for the product name with association to vulnhub or Hackthebox 
> sometimes these are 1:1 as the lab practice for example apache + postfix + vulnhub > google result shows dedicated write up for this exact match.

Recon tips:
If a specific web app doesn't seem to have any directories exposed - 
try to test the name of the domain/subdomain as a potential directory.
OR
CMS name/ forum name/ users / other indicators. 
e.g. > target.e231.com/e231 or  target.e231.com/target

- make note of versions and footer of page for example.. 2012-2017 + on page CMS XYZ - 2017  -> varify version 

# some machines have their own user restrictions.. so not always you will be able to view the flag.txt with just cat.. 
here are some nice alternatives that worked for me during similar vulnhubs, ctf's.

Viewing flag.txt files
If  can't open or view 
try cat -A 
head <filename>
less <filename>
tail -f <filename>
more <filename>

try open file with editors
vi <filename>
vim <filename>
emacs <filename>
nano <filename>
gedit  (gnome's default editor)
leafpad (lxde's default editor)
kedit  (KDE's default editor)
xdg-open <filename>

if viewing doesnt work at all - download to local machine 


Exam tipsfrom reddit

1. Do the buffer overflow first
A: enumerate more or google a way to enumerate the specific service differently
B: think of how what you enumerated > can you chain together to get a shell or sensitive information (service_xyz vuln + service_ttt vuln = the specfic exploit that works 
C: read the exploit you're using and see if it needs editing (based on target info)
2. Realize when your going down a rabbit hole. (exploitation, priv esc...)
3. Have a solid methodology for testing.
