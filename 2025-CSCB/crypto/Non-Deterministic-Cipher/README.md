# Challenge description

Hello, my name is Pollux Moore. I have a fascination with algorithms, unpredictability, non-determinism and especially those mathematical relations where one input can map to multiple outputs!
Inspired by this concept, I’ve created what I call an "unbreakable" cipher.
From a single plaintext, you can generate many different ciphertexts!
To show you this, I’ve generated two different ciphertexts from the same plaintext.
Your task is to recover the original message hidden in it:

FEIHLGEEKJHFDK{EAAEKEJHKEDEJFLFHEKDJJFIBFHJDKIBDDGHFBAEDGKGJDHLEHDIJK_FALAAIJIBDJEBDGECHDHIFB_IHHDKHDALAK_IEKIJJIICJC_IEIECGIAAFKEFAGBHEEDKEEGFABDIE}

AGJDCDEGBADJGC{DJFHBGAHBDDGIJLAHGKGIAIACIGJDLFCGDDGFLAGDGLGJEGCGDGAFL_JFCJIFJJKDFEBEEELEDEIIC_IHGDLHHJKIC_JDBFJFIIBJB_IHAEKEFAIFKDJADBGHDEKHGHFFLEAD}

Note: I didn't have time to encrypt the symbols from the flag, so I added the "{" and "_" later, after the encryption process.

# Soluce

With the given description, we know that is with `Pollux Cipher` that the flag was encrypted.

Pollux Cipher works with morse. You transform a text in morse, and then letters of the alphabet are a `.` or `-` or a `end of letter`. We know that the beginning of the flag is `CSC`. The morse code of `CSC` is `-.-. ... -.-.`. We can do a correspondence table:

```sh
F --> -
E --> .
I --> -
H --> .
L --> EOL
G --> .
K --> EOL
J --> -
D --> .
```

So when we replace in the first ciphertext, we get:

```sh
-.-. ... -.-. {.AA. .-. ...-- -.. .----B-.-. -B....-BA... .-.. ...-- _-A AA---B.-.B...C...--B_-... ..A A _-. -----C-C_-.-.C.-AA- .-A.B.... ...-AB.-.}
```

We don't have the value of `A`, `B` and `C`. We will check in the second ciphertext:

```sh
A --> -
G --> .
J --> -
D --> .
C --> EOL
E --> .
B --> EOL
```

Now let's see what is at the second position after the `{` in the second ciphertext. It's a `J`. And in the second correspondence table, `J` is `-`. In the first cyphertext, there is a `A` in the second position, so we can replace the `A` in the first ciphertext by `-`: 

```sh
-.-. ... -.-. {.--. .-. ...-- -.. .----B-.-. -B....-B-... .-.. ...-- _-- -----B.-.B...C...--B_-... ..- - _-. -----C-C_-.-.C.---- .--.B.... ...--B.-.}
```

Now, since the maximum size of a Morse code letter is 5, we can guess that B and C will be EOL:

```sh
-.-. ... -.-. {.--. .-. ...-- -.. .---- -.-. - ....- -... .-.. ...-- _-- ----- .-. ... ...-- _-... ..- - _-. ----- - _-.-. .---- .--. .... ...-- .-.}
```

Now we can replace the morse code by the corresponding letters:

So the flag is `CSC{PR3D1CT4BL3_M0RS3_BUT_N0T_C1PH3R}`.