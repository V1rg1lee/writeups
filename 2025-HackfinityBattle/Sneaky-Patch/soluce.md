# Challenge description

A high-value system has been compromised. Security analysts have detected suspicious activity within the kernel, but the attacker’s presence remains hidden. Traditional detection tools have failed, and the intruder has established deep persistence. Investigate a live system suspected of running a kernel-level backdoor.



# Soluce

Let's start by checking the system information using the following commands:

```sh
ubuntu@tryhackme:~$ uname -a
lsmod
dmesg | grep -iE "error|warn|fail|panic|oops"
uptime
Linux tryhackme 6.8.0-1016-aws #17-Ubuntu SMP Mon Sep  2 13:48:07 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
Module                  Size  Used by
spatch                 12288  0
8021q                  45056  0
garp                   20480  1 8021q
mrp                    20480  1 8021q
stp                    12288  1 garp
llc                    16384  2 stp,garp
crct10dif_pclmul       12288  1
crc32_pclmul           12288  0
polyval_clmulni        12288  0
polyval_generic        12288  1 polyval_clmulni
ghash_clmulni_intel    16384  0
sha256_ssse3           32768  0
sha1_ssse3             32768  0
aesni_intel           356352  0
crypto_simd            16384  1 aesni_intel
cryptd                 24576  2 crypto_simd,ghash_clmulni_intel
psmouse               217088  0
ena                   151552  0
input_leds             12288  0
serio_raw              20480  0
binfmt_misc            24576  1
sch_fq_codel           24576  3
dm_multipath           45056  0
msr                    12288  0
parport_pc             53248  0
ppdev                  24576  0
lp                     32768  0
parport                73728  3 parport_pc,lp,ppdev
efi_pstore             12288  0
nfnetlink              20480  2
ip_tables              32768  0
x_tables               65536  1 ip_tables
autofs4                57344  2
dmesg: read kernel buffer failed: Operation not permitted
 15:44:48 up 2 min,  2 users,  load average: 0.62, 0.49, 0.20
```

The system is running a custom kernel version 6.8.0-1016-aws. The `lsmod` command shows the loaded kernel modules, and the `dmesg` command displays kernel messages. The `uptime` command shows the system uptime and load average.

There is a suspicious module named `spatch` loaded into the kernel. We can investigate this module further by extracting the module file and analyzing its contents.

```sh
ubuntu@tryhackme:~$ sudo /sbin/modinfo spatch
sudo lsmod | grep spatch
sudo find / -name "*spatch*.ko" 2>/dev/null
filename:       /lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko
description:    Cipher is always root
author:         Cipher
license:        GPL
srcversion:     81BE8A2753A1D8A9F28E91E
depends:        
retpoline:      Y
name:           spatch
vermagic:       6.8.0-1016-aws SMP mod_unload modversions 
spatch                 12288  0
/usr/lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko
ubuntu@tryhackme:~$ 
```

We can analyse the module file (`/usr/lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko
`) using the following command:

```sh
ubuntu@tryhackme:~$ sudo strings /usr/lib/modules/6.8.0-1016-aws/kernel/drivers/misc/spatch.ko | grep -iE 'password|backdoor|shell|exec|root|magic|hide|cmd'
/root/src/spatch.c
HOME=/root
3[CIPHER BACKDOOR] Failed to create /proc entry
6[CIPHER BACKDOOR] Module loaded. Write data to /proc/%s
6[CIPHER BACKDOOR] Module unloaded.
3[CIPHER BACKDOOR] Failed to read output file
6[CIPHER BACKDOOR] Command Output: %s
3[CIPHER BACKDOOR] No output captured.
6[CIPHER BACKDOOR] Executing command: %s
3[CIPHER BACKDOOR] Failed to setup usermode helper.
6[CIPHER BACKDOOR] Format: echo "COMMAND" > /proc/cipher_bd
6[CIPHER BACKDOOR] Try: echo "%s" > /proc/cipher_bd
6[CIPHER BACKDOOR] Here's the secret: 54484d7b73757033725f736e33346b795f643030727d0a
description=Cipher is always root
vermagic=6.8.0-1016-aws SMP mod_unload modversions 
%call_usermodehelper_exec
Ycmd
group_exec_task
prev_sum_exec_runtime
mnt_root
exec_vm
uring_cmd_iopoll
READ_IMPLIES_EXEC
exec_start
exec_update_lock
ma_root
uring_cmd
s_magic
call_usermodehelper_exec
sum_exec_runtime
s_roots
s_root
kernfs_root
exec_max
pp_magic
self_exec_id
io_uring_cmd
root
formatted_cmd
execute_command
in_execve
rb_root
parent_exec_id
last_sum_exec_runtime
execute_only_pkey
rb_root_cached
DQF_ROOT_SQUASH_B
group_exec_task
prev_sum_exec_runtime
mnt_root
exec_vm
uring_cmd_iopoll
READ_IMPLIES_EXEC
exec_start
exec_update_lock
ma_root
uring_cmd
s_magic
sum_exec_runtime
s_roots
s_root
kernfs_root
exec_max
pp_magic
self_exec_id
io_uring_cmd
root
in_execve
rb_root
parent_exec_id
last_sum_exec_runtime
execute_only_pkey
__UNIQUE_ID_vermagic250
rb_root_cached
DQF_ROOT_SQUASH_B
/root/src/spatch.c
/root/src
/root/src/spatch.mod.c
/root/src
__UNIQUE_ID_vermagic250
__pfx_execute_command
call_usermodehelper_exec
```

The module file contains strings related to backdoors, shells, and commands. The string `Here's the secret: 54484d7b73757033725f736e33346b795f643030727d0a` is likely the flag. We can decode this string to obtain the flag.

```sh
ubuntu@tryhackme:~$ echo "54484d7b73757033725f736e33346b795f643030727d0a" | xxd -r -p
THM{sup3r_sn34ky_d00r}
```

So the flag is `THM{sup3r_sn34ky_d00r}`.