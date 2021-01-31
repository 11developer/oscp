# Cross-Compilation exploits
~~~
sudo apt-get install mingw-w64
~~~
# C
~~~
i686-w64-mingw32-gcc hello.c -o hello32.exe      # 32-bit
x86_64-w64-mingw32-gcc hello.c -o hello64.exe    # 64-bit
~~~ 
# C++
~~~
i686-w64-mingw32-g++ hello.cc -o hello32.exe     # 32-bit
x86_64-w64-mingw32-g++ hello.cc -o hello64.exe   # 64-bit
~~~

# Identifying if C code is for Windows or Linux
~~~
C # includes will indicate which OS should be used to build the exploit.
~~~
Command & Description

process.h, string.h, winbase.h, windows.h, winsock2.h

Description Windows exploit code

arpa/inet.h, fcntl.h, netdb.h, netinet/in.h, 
 sys/sockt.h, sys/types.h, unistd.h
~~~
Linux exploit code
Build Exploit GCC

Compile exploit gcc.

Command & Description

#gcc -o exploit exploit.c

Description Basic GCC compile
GCC Compile 32Bit Exploit on 64Bit Kali

Handy for cross compiling 32 bit binaries on 64 bit attacking machines.

Command & Description

#gcc -m32 exploit.c -o exploit

Cross compile 32 bit binary on 64 bit Linux

Compile Windows .exe on Linux

Build / compile windows exploits on Linux, resulting in a .exe file.

Command & Description

#i586-mingw32msvc-gcc exploit.c -lws2_32 -o exploit.exe

Compile windows .exe on Linux
