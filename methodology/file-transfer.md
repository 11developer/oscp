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
