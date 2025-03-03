# Challenge description

In the middle of our conversation, some packets went amiss. We managed to resend a few but they were slightly altered.
Help me reconstruct the message and I'll reward you with something useful ;)

Authors:
Bhakti @debugger0145
Dhanashri @dhanashrib_15632


# Soluce

I start by doing a strings on the pcap file on the known flag format. Once I have the first part, I search for the second part.

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ strings chitty-chat.pcapng | grep -i "vishwa"                         
VishwaCTF{this_is_first_part

┌──(kali㉿kali)-[~/Downloads]
└─$ strings chitty-chat.pcapng | grep -i "part"  
_this_second_part}
VishwaCTF{this_is_first_part
```

So the flag is `VishwaCTF{this_is_first_part_this_second_part}`