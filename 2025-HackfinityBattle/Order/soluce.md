# Challenge description


We intercepted one of Cipher's messages containing their next target. They encrypted their message using a repeating-key XOR cipher. However, they made a critical error—every message always starts with the header:

ORDER:

Can you help void decrypt the message and determine their next target?
Here is the message we intercepted:

1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373

1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60

# Soluce

This is a repeating-key XOR cipher, and we can exploit the fact that the message always begins with "ORDER:" to recover the key and decrypt the message.
Steps to decrypt:

1. Convert the encrypted message into bytes.
2. Use the known prefix "ORDER:" to recover the repeating XOR key.
3. Decrypt the rest of the message by applying this XOR key.

We can do this with [this script](code/order.py).

This gives us:

```sh
┌──(virgile㉿localhost)-[~/Documents/writeups]
└─$ python3 order.py
b'ORDER: Attack at dawn. Target: THM{the_hackfinity_highschool}.'
```

So the flag is `THM{the_hackfinity_highschool}`.